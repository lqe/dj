from django.db import models
from datetime import datetime

class BooksAppRouter(object):
    ''''''
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'books' :
            return 'dj1'
        return None
    db_for_write = db_for_read

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'books' and \
           obj2._meta.app_label == 'books':
            return True
        return None
    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'books':
            return db == 'dj1'
        return None


class BookTest1(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        db_table = 'book_test1'


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        db_table = 'publisher'
        ordering = ["-name"]

    def __unicode__(self):
        return self.name

class Author(models.Model):
    salution = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

    class Meta:
        db_table = 'author'

    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(default=datetime.now)

    class Meta:
        db_table = 'book'

    def __unicode__(self):
        return self.title