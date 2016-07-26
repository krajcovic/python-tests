import os

from django.conf import settings
from django.contrib import admin
from polls.models import Question, Choice


# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    list_per_page = settings.DJANGO_ADMIN_QUESTION_LIST_PER_PAGE


admin.site.register(Question, admin_class=QuestionAdmin)
# admin.site.register(Choice)
