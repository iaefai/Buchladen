from django import template
from store.models import Book

register = template.Library()

@register.inclusion_tag('store/hello.html')
def booklist():
    return { 'message': 'hello' }
