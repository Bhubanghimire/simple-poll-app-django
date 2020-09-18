from django.contrib import admin
from .models import Question,Choice

# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text']

    list_display = ('question_text', 'pub_date','was_publish_recently')

    fieldsets = [
        (None, {'fields':["question_text"]}),
        ('date information',{'fields':['pub_date']})
    ]
    inlines = [ChoiceInline]

    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
