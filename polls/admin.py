from django.contrib import admin

from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

# This gives Question objects an admin interface
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInLine]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # references @admin.display in models.py
    # because it's a DateTimeField, django adds relevant filters
    list_filter = ['pub_date']
    
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
