from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic

from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response


from store.models import Book
from django.core.mail import send_mail

from store.forms import ContactForm, LoginForm
#from store.tags import *

from django.contrib.auth.models import User

class IndexView(generic.ListView):
    template_name = 'store/index.html'
    #context_object_name = 'latest_poll_list'

    def get_queryset(self):
    #    """Return the last five published polls."""
    #    return Poll.objects.order_by('-pub_date')[:5]
        return []



def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/ok')
    else:
        form = LoginForm()

    return render(request, 'store/index.html', { 'form': form })

def login_user(request):
    state = "Please login below..."
    username = password = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in."
            else:
                state = "Your account is not active."
        else:
            state = "Your username / password is not correct."

    return render_to_response('store/auth.html',
                              {'state': state, 'username': username},
                              context_instance = RequestContext(request))


def book_list(request):
    state = "Booklist page..."
    book_list = Book.objects.all()
    return render_to_response('store/book_list.html',
                              {'state': state, 'book_list': book_list, 'title_banner': 'Book List'})

def contact_seller(request):
    user = request.GET.get('id', 'NO_USER_SPECIFIED');
    bookname = request.GET.get('bookname', 'NO_BOOK_SPECIFIED');
    form = contact_form();
    return render_to_response('store/contact_seller.html',
                              {'user': user, 'bookname':bookname, 'form': form},context_instance = RequestContext(request))

def email_send(request):
    this_id = request.GET.get('id', 'NO_USER_SPECIFIED');
    bookname = request.GET.get('book', 'NO_BOOK_SPECIFIED');
    reply_email = request.POST.get('reply_email','NO_REPLY_EMAIL');
    message = request.POST.get('message','NO_MESSAGE');
    user = User.objects.get(id=this_id);
    email = user.email;
    subject = 'Buchladen: Someone is interested in your book "'+bookname+'"!';
    message = message+" TO REPLY TO THIS USER, USE THE PROVIDED EMAIL: "+reply_email;
    #send_mail(subject, message, 'noreply@buchladen.uwinsocr.ca',[email], fail_silently=False);
    return render_to_response('store/email-sent.html',
                              {'user': this_id,'message': message, 'subject': subject},context_instance = RequestContext(request))
        
def isbn(request, isbn_number):
    state = "isbn result page"
    books = []
    target = isbn_number
    for book in Book.objects.all():
        if book.isbn == target:
            books.append(book)
        elif "978"+target == book.isbn:
            books.append(book)
    return render_to_response('store/book_list.html',
                              {'state': state, 'book_list': books, 'title_banner': 'Isbn Results'})


def author(request, author_name):
    state = "author result page"
    books = []
    target = author_name.lower()
    for book in Book.objects.all():
        for authors in book.authors.all():
            if target in authors.name.lower():
                books.append(book)
    return render_to_response('store/book_list.html',
                              {'state': state, 'book_list': books, 'title_banner': 'Author Results'})


def title(request, title_name):
    state = "title result page"
    books = []
    target = title_name.lower()
    for book in Book.objects.all():
        if target in book.title.lower():
            books.append(book)
    return render_to_response('store/book_list.html',
                              {'state': state, 'book_list': books, 'title_banner': 'Title Results'})
        
