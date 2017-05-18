# import datetime
from django.db import models
# from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField('问题',max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    #自定义
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField('选择',max_length=200)
    votes = models.IntegerField('投票',default=0)

    def __str__(self):
        return self.choice_text

