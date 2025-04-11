from django.contrib import admin

# Register your models here.
from .models import  Choice, Question

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3 # number of empty choice fields to display

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)