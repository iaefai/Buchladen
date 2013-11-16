import re

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = 'search string'
    help = 'Test search of the database'

    def handle(self, *args, **options):
        try:
            input = args[0]
            print("Got string %s \n" % input)
            searcher = SearchTerms(input)
            searcher.output()


        except e:
            print("Error %s.\n" % e)

class SearchTerms:
    authors = []
    subjects = []
    titles = []
    keywords = []
    isbn = []

    def __init__(self, s):
        self.parse(s)

    def parse(self, s):
        keyword = re.compile(r'(?P<words>\w+|"[^"]*")')
        author = re.compile('author:' + keyword.pattern)
        subject = re.compile('subject:' + keyword.pattern)
        title = re.compile('title:' + keyword.pattern)
        isbn = re.compile('isbn:(?P<words>[0-9-]+)')


        while 1:
            s = s.lstrip()
            print("string: '%s'" % s)
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








def largest_match(matches):
    matches = (item for item in matches if item is not None)
    if len(matches) == 0:
        return None
    else:
        max = matches[0].end() - matches[0].start()
        max_match = matches[0]

        for m in matches:
            size = m.end() - m.start()
            if (size > max):
                max_match = m
                max = size

        return max




