from django.contrib import admin
from .models import Question, Choice
# Register your models here.

#有关联的可以值注册一个
#StackedInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields':['question_text']}),
        ('日期信息', {'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question,QuestionAdmin)