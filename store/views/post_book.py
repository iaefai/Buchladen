
from store.forms import BookForm
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.views.generic import View
from store.models import *
from django.http import HttpResponse
import datetime

import logging

logger = logging.getLogger(__name__)

class Post(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            title = request.POST['title']
            authors = request.POST['authors']
            isbn = request.POST['isbn']
            subjects = request.POST['subjects']
            publisher = request.POST['publisher']
            price = request.POST['price']

            logger.info("title: %s" % title)
            logger.info("authors: %s" % authors)
            logger.info("isbn: %s" % isbn)
            logger.info("subjects: %s" % subjects)
            logger.info("publisher: %s" % publisher)
            logger.info("price: %s" % price)


            book, created = Book.objects.get_or_create(title = title,
                                                       isbn = isbn,
                                                       publisher = publisher,
                                                       price = float(price),
                                                       user = request.user,
                                                       date_added = datetime.date.today())

            if created:
                author_list = authors.split(sep=";,")
                subject_list = subjects.split(sep=None)

                authors = []
                for author in author_list:
                    a, created = Author.objects.get_or_create(name = author)
                    authors.append(a)

                subjects = []
                for subject in subject_list:
                    s, created = Subject.objects.get_or_create(subject = subject)
                    subjects.append(s)

                book.authors = authors
                book.subjects = subjects
                book.save()

            return HttpResponse("created book")
        else:
            return HttpResponse("not logged in")
