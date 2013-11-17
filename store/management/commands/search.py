

from django.core.management.base import BaseCommand, CommandError
from store.search import *

class Command(BaseCommand):
    args = 'search string'
    help = 'Test search of the database'

    def handle(self, *args, **options):
        try:
            input = args[0]
            print("Got string %s \n" % input)
            searcher = SearchTerms(input)
            searcher.output()

            print("\nResults:")
            results = Search(searcher).results()
            print(list(results))

        except Exception as e:
            print("Error %s.\n" % e)





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




