__author__ = 'stephen'

from django.test import TestCase
from django.core.urlresolvers import reverse
from store.models import *
import datetime
from decimal import Decimal
from store.urls import urlpatterns


class WebPageTester(TestCase):
    def test_web_pages(self):
        argument_pages = ["author", "title", "isbn"]
        for url in urlpatterns:
            if url.name in argument_pages:
                response = self.client.get(reverse("store.views."+url.name, args=['90']))
            else:
                response = self.client.get(reverse("store.views."+url.name))
            self.assertEqual(response.status_code, 200)
    

class BookTest(TestCase):
    fixtures = ['test_database.json']

    def test_title(self):
        titles = ["The Complete Guide to C++", "The Debutante's Fall", "Candy"]
        for k in 0, 1, 2:
            store_1 = Book.objects.get(pk=(k+1))
            self.assertEqual(store_1.title, titles[k])

    def test_authors(self):
        authors = ["Anton Szandor Lavey", "Stephen Brooks", "Huck Pilgrim", "Kevin Brooks"]
        self.assertEqual(Book.objects.get(pk=1).authors.count(), 2)
        self.assertEqual(Book.objects.get(pk=2).authors.count(), 1)
        self.assertEqual(Book.objects.get(pk=3).authors.count(), 1)
        k = 0
        for books in Book.objects.all():
            for author in books.authors.all():
                self.assertEqual(author.name, authors[k])
                k += 1

    def test_subjects(self):
        subjects = ["Truth", "Computer Science", "Fiction", "Fiction"]
        self.assertEqual(Book.objects.get(pk=1).subjects.count(), 2)
        self.assertEqual(Book.objects.get(pk=2).subjects.count(), 1)
        self.assertEqual(Book.objects.get(pk=3).subjects.count(), 1)
        k = 0
        for books in Book.objects.all():
            for subject in books.subjects.all():
                self.assertEqual(subject.subject, subjects[k])
                k += 1

    def test_isbn(self):
        isbn = ["978-0380015399", "B00DGVFO4M", "0439683289"]
        k = 0
        for books in Book.objects.all():
            self.assertEqual(books.isbn, isbn[k])
            k += 1

    def test_price(self):
        prices = [Decimal('7.19'), Decimal('16.99'), Decimal('6.95')]
        k = 0
        for books in Book.objects.all():
            self.assertEqual(books.price, prices[k])
            k += 1

    def test_data_added(self):
        date_added = [datetime.date(2013, 10, 15), datetime.date(2013, 10, 16), datetime.date(2011, 11, 15)]
        k = 0
        for books in Book.objects.all():
            self.assertEqual(books.date_added, date_added[k])
            k += 1

    def test_user(self):
        #TODO: redo this test once real users are in the database and not just [test] users
        users_id = [2,      2,      2]
        k = 0
        for books in Book.objects.all():
            self.assertEqual(books.user_id, users_id[k])
            k += 1
