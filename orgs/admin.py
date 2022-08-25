from django.contrib import admin

from orgs.models import Organisation, OrganisationMembership


class OrganisationMembershipInlineAdmin(admin.StackedInline):
    model = OrganisationMembership
    extra = 0


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    inlines = [OrganisationMembershipInlineAdmin]
