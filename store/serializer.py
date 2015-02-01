from nap import models, serialiser
from django.contrib.auth.models import User

from .models import Subject, Author, Book

class SubjectSerializer(serialiser.ModelSerialiser):
    class Meta:
        model = Subject

class AuthorSerializer(serialiser.ModelSerialiser):
    class Meta:
        model = Author

class BookSerializer(serialiser.ModelSerialiser):
    authors  = serialiser.ModelManySerialiserField('authors.all', model=Author)
    subjects = serialiser.ModelManySerialiserField('subjects.all', model=Subject)
    user = serialiser.ModelSerialiserField(model=User)
    class Meta:
        model = Book

class UserSerializer(serialiser.ModelSerialiser):
    class Meta:
        model = User
