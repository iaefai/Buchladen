from django.db.models.query import QuerySet

from store.models import *
import re

class Search:
    def __init__(self, terms):
        self.terms = terms

    def results(self):
        res = Book.objects.all()

        for title in self.terms.titles:
            booklist = Book.objects.filter(title__icontains = title)
            print("title keyword %d" % booklist.count())
            res &= booklist

        for author in self.terms.authors:
            authors = Author.objects.filter(name__icontains = author)
            booklist = Book.objects.filter(authors__in = authors)
            print("author keyword %d " % booklist.count())
            res &= booklist

        for subject in self.terms.subjects:
            subjects = Subject.objects.filter(subject__icontains = subject)
            booklist = Book.objects.filter(subjects__in = subjects)
            print("subjects keyword %d " % booklist.count())
            res &= booklist

        for num in self.terms.isbn:
            booklist = Book.objects.filter(isbn__icontains = num)
            print("isbn keyword: %d" % booklist.count())
            res &= booklist

        for word in self.terms.keywords:
            booklist = Book.objects.filter(isbn__icontains = word)
            print(" isbn: %d" % booklist.count())
            booklist |= Book.objects.filter(title__icontains = word)
            print(" title: %d" % booklist.count())
            subjects = Subject.objects.filter(subject__icontains = word)
            booklist |= Book.objects.filter(subjects__in = subjects)
            print(" subjects: %d" % booklist.count())

            authors = Author.objects.filter(name__icontains = word)

            booklist |= Book.objects.filter(authors__in = authors)
            print(" authors: %d" % booklist.count())

            res &= booklist
        #if self.terms.titles is not []:
        #    booklist = Book.objects.filter(title__in = self.terms.titles)
        #
        #if self.terms.isbn is not []:
        #    isbn_results = Book.objects.filter(isbn__in = self.terms.isbn)
        return res.distinct()


class SearchTerms:
    def __init__(self, s):
        self.authors = []
        self.subjects = []
        self.titles = []
        self.keywords = []
        self.isbn = []
        self.parse(s)

    def parse(self, s):
        #keyword = re.compile(r'(?P<words>(\W|[^:])+|"[^"]*")')
        keyword = re.compile(r'(?P<words>(\w|[+-])+|"[^"]*")')
        author = re.compile('author:' + keyword.pattern)
        subject = re.compile('subject:' + keyword.pattern)
        title = re.compile('title:' + keyword.pattern)
        isbn = re.compile('isbn:(?P<words>[0-9-]+)')


        while 1:
            s = s.lstrip()
            author_ = author.match(s)
            subject_ = subject.match(s)
            title_ = title.match(s)
            keyword_ = keyword.match(s)
            isbn_ = isbn.match(s)

            if (author_ is not None):
                self.authors.append(author_.group("words"))
                s = s[author_.end():]
            elif (subject_ is not None):
                self.subjects.append(subject_.group("words"))
                s = s[subject_.end():]
            elif (title_ is not None):
                self.titles.append(title_.group("words"))
                s = s[title_.end():]
            elif (isbn_ is not None):
                self.isbn.append(isbn_.group("words"))
                s = s[isbn_.end():]
            elif (keyword_ is not None):
                self.keywords.append(keyword_.group("words"))
                s = s[keyword_.end():]
            else:
                break

    def output(self):
        print("Authors:")

        for i in self.authors:
            print("   " + i)

        print("Subjects:")

        for i in self.subjects:
            print("   " + i)

        print("Titles:")

        for i in self.titles:
            print("   " + i)

        print("ISBN:")

        for i in self.isbn:
            print("   " + i)

        print("Keywords:")

        for i in self.keywords:
            print("   " + i)




