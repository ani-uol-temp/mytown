from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from feedbacks.forms import FeedbackNoteForm
from feedbacks.models import Feedback, FeedbackNote


class PermissionRequiredMixin:
    permissions = []

    def has_all_permissions(self):
        return self.request.user.has_perms(self.permissions)

    def dispatch(self, request, *args, **kwargs):
        # if not self.request.user:
        #     raise PermissionDenied("You need to be logged in.")

        if not self.has_all_permissions():
            raise PermissionDenied("You do not have permissions to perform: " + ", ".join(self.permissions))

        return super().dispatch(request, *args, **kwargs)


class FeedbackUpdateView(PermissionRequiredMixin, SuccessMessageMixin, DetailView):
    permissions = ['change_feedback']

    model = Feedback
    template_name = 'feedbacks/feedback_update.html'
    success_url = '/feedbacks/update'
    success_message = "Your Feedback (ID %(calculated_field)s) was created successfully! " \
                      "Please keep track of your ID for future enquiries."

    def get_queryset(self):
        return super().get_queryset().prefetch_related('feedbacknote_set')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.update_state()

        return super().get(request, *args, **kwargs)

    def update_state(self):
        action = self.request.POST.get('action')
        available_actions = map(lambda a: a.name,
                                self.object.get_available_user_status_transitions(user=self.request.user))
        if action in available_actions:
            getattr(self.object, action)()
        self.object.save()

    def get_success_url(self):
        return reverse('feedback-detail', kwargs={'pk': self.object.id})

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.id,
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['transitions'] = self.object.get_available_user_status_transitions(user=self.request.user)
        return ctx


class FeedbackNoteCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permissions = ['add_feedbacknote']
    model = FeedbackNote
    form_class = FeedbackNoteForm
    template_name = 'feedbacks/feedback_note_create.html'
    success_message = "Your Note was recorded successfully."

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['feedback'] = get_object_or_404(Feedback, pk=self.kwargs['pk'])
        return ctx

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['feedback_id'] = self.kwargs['pk']
        return kwargs

    def get_success_url(self):
        return reverse('feedback-update', kwargs={'pk': self.kwargs['pk']})
