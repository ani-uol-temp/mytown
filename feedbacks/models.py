import uuid

from django.conf import settings
from django.db import models
from django_fsm import FSMField, transition
from django.utils.translation import gettext_lazy as _


class FeedbackStatus(models.TextChoices):
    NEW = 'new', _('New')
    ASSESSING = 'assessing', _('Assessing')
    WORK_IN_PROGRESS = 'in_progress', _('Work In Progress')
    RESOLVED = 'resolved', _('Resolved')
    CLOSED = 'closed', _('Closed')
    INVALID = 'invalid', _('Invalid')


class Feedback(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=255, help_text=_('A short title summarising your report.'))
    description = models.TextField(help_text=_('A description of what happened.'))

    photo_1 = models.ImageField(blank=True, null=True, default=None, verbose_name=_('Photo 1 (Optional)'))
    photo_2 = models.ImageField(blank=True, null=True, default=None, verbose_name=_('Photo 2 (Optional)'))
    photo_3 = models.ImageField(blank=True, null=True, default=None, verbose_name=_('Photo 3 (Optional)'))

    status = FSMField(default=FeedbackStatus.NEW)

    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE)

    organisation = models.ForeignKey('orgs.Organisation', on_delete=models.PROTECT,
                                     related_name='feedbacks', blank=True, null=True)

    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                                    related_name='assigned_feedbacks', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @transition(field=status, source=FeedbackStatus.NEW, target=FeedbackStatus.CLOSED)
    def close(self):
        pass

    @transition(field=status, source=FeedbackStatus.NEW, target=FeedbackStatus.INVALID)
    def mark_invalid(self):
        pass

    @transition(field=status, source=FeedbackStatus.NEW, target=FeedbackStatus.ASSESSING)
    def mark_assessing(self):
        pass

    @transition(field=status, source=FeedbackStatus.ASSESSING, target=FeedbackStatus.WORK_IN_PROGRESS)
    def mark_work_in_progress(self):
        pass

    @transition(field=status, source=[FeedbackStatus.WORK_IN_PROGRESS, FeedbackStatus.ASSESSING],
                target=FeedbackStatus.RESOLVED)
    def resolve(self):
        pass

    @transition(field=status, source=[FeedbackStatus.CLOSED],
                target=FeedbackStatus.ASSESSING)
    def reopen(self):
        pass

    def __str__(self):
        return self.title


class FeedbackVisibility(models.TextChoices):
    PUBLIC = 'public', _('Public')
    INTERNAL = 'internal', _('Internal')


class FeedbackNoteManager(models.Manager):
    def public_only(self):
        return self.filter(visibility=FeedbackVisibility.PUBLIC)


class FeedbackNote(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    visibility = models.CharField(max_length=10, choices=FeedbackVisibility.choices,
                                  default=FeedbackVisibility.INTERNAL)
    feedback = models.ForeignKey('Feedback', on_delete=models.CASCADE)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = FeedbackNoteManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    associated_organisation = models.ForeignKey(
        'orgs.Organisation',
        on_delete=models.PROTECT,
        related_name='categories'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
