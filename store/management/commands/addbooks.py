from django.core.management.base import BaseCommand, CommandError
from store.search import *
from django.contrib.auth.models import *

import datetime
import traceback
import sys

import urllib.request
import json

from store.models import *

class Command(BaseCommand):
    args = 'search string for book subject'
    help = 'Adds a set of books from isbndb'

    def handle(self, *args, **options):
        try:
            input = args[0]
            print("Got string %s \n" % input)


            data = open("/Users/drakej/.isbndbkey").read().strip()
            #print("key: <%s>" % data)
            url = "http://isbndb.com/api/v2/json/%s/books?q=%s" % (data, input)
            #&i=author_name
            request = urllib.request.urlopen(url)
            data = request.read().decode("utf-8")
            bookdata = json.loads(data)

            #print(data.decode("utf-8"))
            #print(bookdata)

            print("Results: %d\n" % len(bookdata["data"]))

            for book in bookdata["data"]:
                subjects = []
                authors = []
                print("Title: %s\n" % book["title"])
                for subject in book["subject_ids"]:
                    sub, created = Subject.objects.get_or_create(subject = subject)
                    if created:
                        sub.save()
                    subjects.append(sub)
                for author in book["author_data"]:
                    auth, created = Author.objects.get_or_create(name = author["name"])
                    if created:
                        auth.save()
                    authors.append(auth)
                b, created = Book.objects.get_or_create(title = book["title"],
                                         # authors = authors,
                                          isbn = book["isbn13"],
                                        #  subjects = subjects,
                                          publisher = book["publisher_text"],
                                          #language = "en",
                                          price = 10.00,
                                          date_added = datetime.date.today(),
                                          user = User.objects.get(username = "drakej"))
                if created:
                    b.authors = authors
                    b.subjects = subjects
                    b.save()


        except Exception as e:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stderr)
            print("-"*60)

