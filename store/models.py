from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.subject

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30)
    #edition = models.CharField(max_length=10)
    authors = models.ManyToManyField(Author)
    #condition = models.CharField(max_length=20)   ## perhaps we need a choice
    isbn = models.CharField(max_length=20)      # no explicit validation yet
    subjects = models.ManyToManyField(Subject)
    publisher = models.CharField(max_length=30)
    language = (('en', "English"), ('cn', "Chinese"), ('kn', "Klingon"))
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateField()
    user = models.ForeignKey(User)
    #description = models.TextField()

    #def default(self):
    #    """
    #    Convert model to JSON
    #    """
    #    dict = {}
    #    dict['title'] = self.title
    #    dict['isbn'] = self.isbn
    #    dict['publisher'] = self.publisher
    #    dict['language'] = self.language
    #    dict['price'] = self.price
    #    dict['date_added'] = self.date_added
    #    dict['user'] = self.user.username
    #    dict['authors'] =

