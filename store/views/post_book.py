
from store.forms import BookForm
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.views.generic import TemplateView

def post_book(request):
    user = 'sup'
    bookname = 'da book'
    form = BookForm()
    return render_to_response('store/post_book.html',
                              {'user': user, 'bookname':bookname, 'form': form},
                              context_instance = RequestContext(request))
