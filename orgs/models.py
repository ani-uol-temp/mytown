import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Organisation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    public_key = models.TextField(blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OrganisationMembershipRoles(models.TextChoices):
    ADMIN = 'admin', _('Admin')
    CASE_OFFICER = 'case_officer', _('Case Officer')


class OrganisationMembership(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    role = models.CharField(max_length=20, choices=OrganisationMembershipRoles.choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organisation = models.ForeignKey('Organisation', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
