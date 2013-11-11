
from django import template

register = template.Library()

print("Registering booklist tag\n")

@register.inclusion_tag('store/booklist.html')
def booklist():
    book_list = Book.objects.all()
    return { 'book_list': book_list }
