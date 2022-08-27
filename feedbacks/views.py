from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, FormView
from rest_framework import viewsets, mixins

from feedbacks.forms import SearchForm
from feedbacks.models import Feedback
from feedbacks.serializers import FeedbackSerializer


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['title', 'description', 'category', 'photo_1', 'photo_2', 'photo_3']
    template_name = 'feedbacks/feedback_create.html'
    success_url = '/feedbacks/new'
    success_message = "Your Feedback (ID %(calculated_field)s) was created successfully! " \
                      "Please keep track of your ID for future enquiries."

    def form_valid(self, form):
        ret = super().form_valid(form)
        self.object.organisation = self.object.category.associated_organisation
        self.object.save()
        return ret

    def get_success_url(self):
        return reverse('feedback-detail', kwargs={'pk': self.object.id})

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.id,
        )


class EnquireFeedbackSearchView(FormView):
    form_class = SearchForm
    template_name = 'feedbacks/feedback_enquiry.html'

    def form_valid(self, form):
        return redirect(
            reverse('feedback-detail', kwargs={'pk': self.get_form().data.get('feedback_id')}),
            permanent=False
        )


class EnquireFeedbackView(DetailView):
    model = Feedback
    context_object_name = 'feedback'
    template_name = 'feedbacks/feedback_view.html'
