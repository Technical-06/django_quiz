from django.contrib import admin
from quiz.models import Quiz

class QuizAdmin(admin.ModelAdmin):
  list_display = [
    'question1',
    'option1',
    'option2',
    'corrans',
  ]

admin.site.register(Quiz)

