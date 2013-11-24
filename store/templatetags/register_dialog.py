
from django import template
from store.models import Book

register = template.Library()


@register.inclusion_tag('store/register_login.html')
def register_dialog():
    #book_list = Book.objects.all()
    #return { 'book_list': book_list }
    return
