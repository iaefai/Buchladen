
from django import template
from store.models import Book

register = template.Library()


@register.inclusion_tag('store/booklist.html')
def booklist():
    book_list = Book.objects.all()
    return { 'book_list': book_list }
