import django_filters

from feedbacks.models import FeedbackStatus, Feedback


class FeedbackFilter(django_filters.FilterSet):
    status = django_filters.MultipleChoiceFilter(choices=FeedbackStatus.choices)

    class Meta:
        model = Feedback
        fields = ['status']
