import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField('问题',max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    #自定义
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)  #这句隐藏这一个bug 就是未来的时间发布的也会返回TRUE  应该返回FALSE
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField('选择',max_length=200)
    votes = models.IntegerField('投票',default=0)

    def __str__(self):
        return self.choice_text

