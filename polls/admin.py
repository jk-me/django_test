from django.contrib import admin

# Register your models here.
from .models import  Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # number of empty choice fields to display

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)