from django.contrib import admin

from feedbacks.models import Feedback, FeedbackNote, FeedbackPhoto


class FeedbackPhotoInlineAdmin(admin.TabularInline):
    model = FeedbackPhoto
    extra = 0
    readonly_fields = ['id']


class FeedbackNoteInlineAdmin(admin.StackedInline):
    model = FeedbackNote
    extra = 0
    readonly_fields = ['id']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    inlines = [FeedbackPhotoInlineAdmin, FeedbackNoteInlineAdmin]
    list_display = ['title', 'status', 'created_at']
    readonly_fields = ['id']
