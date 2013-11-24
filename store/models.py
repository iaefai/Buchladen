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
    title = models.CharField(max_length=70)
    #edition = models.CharField(max_length=10)
    authors = models.ManyToManyField(Author)
    #condition = models.CharField(max_length=20)   ## perhaps we need a choice
    isbn = models.CharField(max_length=20)      # no explicit validation yet
    subjects = models.ManyToManyField(Subject)
    publisher = models.CharField(max_length=30)
    #language = (('en', "English"), ('cn', "Chinese"), ('kn', "Klingon"))
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateField()
    user = models.ForeignKey(User)

    # for admin:
    def author_names(self):
        return ', '.join([a.name for a in self.authors.all()])
    author_names.short_description = "Author Names"

    def subject_list(self):
        return ', '.join([a.subject for a in self.subjects.all()])
    subject_list.short_description = "Subjects"

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.OneToOneField(User)
    phoneNumber = models.CharField(max_length=14)

