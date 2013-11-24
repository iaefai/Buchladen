from django import forms
from django.forms import ModelForm
from store.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ['user','date_added']
