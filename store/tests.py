__author__ = 'stephen'

from django.test import TestCase
from django.core.urlresolvers import reverse
from store.models import *
import datetime
from decimal import Decimal
from store.urls import urlpatterns

# TODO: this got broken in the new django version, will have to redo.
#class WebPageTester(TestCase):
#    def test_web_pages(self):
#        argument_pages = ["author", "title", "isbn"]
#        for url in urlpatterns:
#            print("hi")
#            response = self.client.get(reverse(url.name))
#            self.assertEqual(response.status_code, 200)
    

class BookTest(TestCase):
    fixtures = ['tests_database.json']

    def test_title(self):
        titles = ["The Complete Guide to C++", "The Debutante's Fall", "Candy", "American Girl", "Summer Shorts", "A Good Girl is an Easy Sacrifi", "China's Human Rights Lawyers a"]
        for k in 0, 1, 2, 3, 4, 5, 6:
            store_1 = Book.objects.get(pk=(k+1))
            self.assertEqual(store_1.title, titles[k])

    def test_authors(self):
        authors = ["Anton Szandor Lavey", "Huck Pilgrim", "Huck Pilgrim", "Kevin Brooks", "Huck Pilgrim", "Huck Pilgrim", "Huck Pilgrim", "Eva Pils"]
        self.assertEqual(Book.objects.get(pk=1).authors.count(), 2)
        self.assertEqual(Book.objects.get(pk=2).authors.count(), 1)
        self.assertEqual(Book.objects.get(pk=3).authors.count(), 1)
        k = 0
        for books in Book.objects.all():
            for author in books.authors.all():
                self.assertEqual(author.name, authors[k])
                k += 1

    def test_subjects(self):
        subjects = ["Truth", "Fiction", "Fiction", "Fiction", "Fiction", "Fiction", "Fiction", "Law"]
        self.assertEqual(Book.objects.get(pk=1).subjects.count(), 2)
        self.assertEqual(Book.objects.get(pk=2).subjects.count(), 1)
        self.assertEqual(Book.objects.get(pk=3).subjects.count(), 1)
        k = 0
        for books in Book.objects.all():
            for subject in books.subjects.all():
                self.assertEqual(subject.subject, subjects[k])
                k += 1

    def test_isbn(self):
        isbn = ["9780380015399", "B00DGVFO4M", "0439683289", "B006SL8CMI", "B005ECBNO6", "B00BZXQ8Z2", "978-0415870849"]
        k = 0
        for books in Book.objects.all():
            self.assertEqual(books.isbn, isbn[k])
            k += 1

    def test_price(self):
        prices = [Decimal('7.19'), Decimal('16.99'), Decimal('6.95'), Decimal('5'), Decimal('6'), Decimal('4.5'), Decimal('100')]
        k = 0
        for books in Book.objects.all():
            self.assertEqual(books.price, prices[k])
            k += 1

    def test_data_added(self):
        date_added = [datetime.date(2013, 10, 15), datetime.date(2013, 10, 15), datetime.date(2013, 10, 15), datetime.date(2013, 11, 10), datetime.date(2013, 11, 10), datetime.date(2013, 11, 10), datetime.date(2013, 11, 10)]
        k = 0
        for books in Book.objects.all():
            self.assertEqual(books.date_added, date_added[k])
            k += 1

    def test_user(self):
        users_id = [4, 5, 5, 1, 1, 1, 1]
        k = 0
        for books in Book.objects.all():
            self.assertEqual(books.user_id, users_id[k])
            k += 1
