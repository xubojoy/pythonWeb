from django.contrib import admin
from .models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields':['question_text']}),
        ('日期信息', {'fields':['pub_date'],'classes':['collapse']}),
    ]


admin.site.register(Question,QuestionAdmin)