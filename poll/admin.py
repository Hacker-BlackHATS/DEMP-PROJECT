from django.contrib import admin
from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
# One small problem, though. It takes a lot of screen space to display all the fields
# for entering related Choice objects.
# For that reason, Django offers a tabular way of displaying inline related objects.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    # You might want to split the form up into fieldsets :
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'],
                              'classes': ['collapse']
                              }
         ),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
