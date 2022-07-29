from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView

from feedbacks.models import Feedback


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    fields = ['title', 'description']
    template_name = 'feedbacks/feedback_create.html'
    success_url = '/feedbacks/new'
    success_message = "Your Feedback (ID %(calculated_field)s) was created successfully!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.id,
        )


def enquire_feedback(request):
    return render(request, 'feedbacks/feedback_enquiry.html', {
        'page_title': 'Enquire Feedback'
    })
