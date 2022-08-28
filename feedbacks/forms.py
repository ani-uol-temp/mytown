from django.core.exceptions import ValidationError
from django.forms import Form, fields, ModelForm, TextInput
from django.utils.translation import gettext_lazy as _

from feedbacks.models import Feedback, FeedbackNote


def validate_feedback_uuid(uuid: str):
    if not Feedback.objects.filter(id=uuid).exists():
        raise ValidationError(_('Provided Feedback ID is not valid.'), code='invalid_id')

    return True


class SearchForm(Form):
    feedback_id = fields.UUIDField(
        validators=[validate_feedback_uuid],
        label='Feedback ID',
        help_text=_('The ID you were given during the anonymous feedback submission.')
    )


class FeedbackNoteForm(ModelForm):
    class Meta:
        model = FeedbackNote
        fields = ['title', 'description', 'visibility']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.feedback_id = kwargs.pop('feedback_id', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.created_by = self.user
        self.instance.feedback_id = self.feedback_id
        return super().save(commit)


class FeedbackCreateForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'description', 'category', 'photo_1', 'photo_2', 'photo_3']
        widgets = {
            'title': TextInput()
        }
