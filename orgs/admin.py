from django.contrib import admin

from feedbacks.models import Category
from orgs.models import Organisation, OrganisationMembership


class OrganisationMembershipInlineAdmin(admin.StackedInline):
    model = OrganisationMembership
    extra = 0


class CategoryInlineAdmin(admin.TabularInline):
    model = Category
    extra = 0
    readonly_fields = ['id']


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    ordering = ['name']
    inlines = [OrganisationMembershipInlineAdmin, CategoryInlineAdmin]
