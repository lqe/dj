import datetime

from django.utils import timezone
from django.db import models

class PollsAppRouter(object):
    ''''''
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'polls' :
            return 'dj2'
        return None
    db_for_write = db_for_read

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'polls' and \
           obj2._meta.app_label == 'polls':
            return True
        return None
    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'polls':
            return db == 'dj2'
        return None

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        db_table = 'question'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text

    class Meta:
        db_table = 'choice'