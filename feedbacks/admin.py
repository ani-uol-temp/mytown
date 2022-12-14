from django.contrib import admin

from feedbacks.models import Feedback, FeedbackNote, Category


class FeedbackNoteInlineAdmin(admin.StackedInline):
    model = FeedbackNote
    extra = 0
    readonly_fields = ['id']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    inlines = [FeedbackNoteInlineAdmin]
    list_display = ['title', 'status', 'created_at']
    readonly_fields = [
        'status', 'id',
        'created_at', 'updated_at',
        'title', 'description',
        'photo_1', 'photo_2', 'photo_3',
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'associated_organisation', 'created_at']
