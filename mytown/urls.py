"""mytown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views import generic
from django.views.generic import TemplateView

from feedbacks.admin_views import FeedbackUpdateView, FeedbackNoteCreateView, FeedbackListView
from feedbacks.views import FeedbackCreateView, EnquireFeedbackView, \
    EnquireFeedbackSearchView, RetrieveCategoryView
from orgs.views import get_public_key

urlpatterns = [
    path(r'', generic.RedirectView.as_view(url='/feedbacks/new', permanent=False)),
    path('admin/', admin.site.urls),
    path('feedbacks/new', FeedbackCreateView.as_view(), name='feedback-new'),
    path('feedbacks/enquire', EnquireFeedbackSearchView.as_view(), name='feedback-search'),
    path('feedbacks/', FeedbackListView.as_view(), name='feedback-list'),
    path('feedbacks/<uuid:pk>', EnquireFeedbackView.as_view(), name='feedback-detail'),
    path('feedbacks/<uuid:pk>/update', login_required(FeedbackUpdateView.as_view()), name='feedback-update'),
    path('feedbacks/<uuid:pk>/notes/new', login_required(FeedbackNoteCreateView.as_view()), name='feedback_note-new'),

    path('encryption/setKey',
         login_required(TemplateView.as_view(template_name='feedbacks/admin/encryption_set_key.html')),
         name='encryption-set-key'),

    path('accounts/', include('allauth.urls')),

    path('api/categories/<uuid:pk>', RetrieveCategoryView.as_view(), name='category-single'),
    path('api/organisations/<uuid:pk>/publicKey', get_public_key, name='get-public-key'),
]

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
