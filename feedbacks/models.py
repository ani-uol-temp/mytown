import uuid

from django.conf import settings
from django.db import models
from django_fsm import FSMField, transition
from django.utils.translation import gettext_lazy as _


class Feedback(models.Model):
    class FeedbackStatus(models.TextChoices):
        NEW = 'new', _('New')
        ASSESSING = 'assessing', _('Assessing')
        WORK_IN_PROGRESS = 'in_progress', _('Work In Progress')
        RESOLVED = 'resolved', _('Resolved')
        CLOSED = 'closed', _('Closed')
        INVALID = 'invalid', _('Invalid')

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = FSMField(default=FeedbackStatus.NEW)

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

    def __str__(self):
        return self.title


class FeedbackPhoto(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    image = models.ImageField()
    feedback = models.ForeignKey('Feedback', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            return self.image.path
        except (AttributeError, TypeError):
            return self.id


class FeedbackNote(models.Model):
    class FeedbackVisibility(models.TextChoices):
        PUBLIC = 'public', _('Public')
        INTERNAL = 'internal', _('Internal')

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    visibility = models.CharField(max_length=10, choices=FeedbackVisibility.choices)
    feedback = models.ForeignKey('Feedback', on_delete=models.CASCADE)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
