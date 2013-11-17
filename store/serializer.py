from nap import models, fields, api, serialiser, publisher
from django.contrib.auth.models import User

from .models import Subject, Author, Book

class SubjectSerializer(models.ModelSerialiser):
    class Meta:
        model = Subject

class AuthorSerializer(models.ModelSerialiser):
    class Meta:
        model = Author

class BookSerializer(models.ModelSerialiser):
    class Meta:
        model = Book

class UserSerializer(models.ModelSerialiser):
    class Meta:
        model = User
