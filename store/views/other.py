from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic

from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response


from store.models import Book, Author
from django.core.mail import send_mail

from store.forms import ContactForm, LoginForm
#from store.tags import *

from django.contrib.auth.models import User
from jsonview.decorators import json_view

from store.search import *
from store.serializer import *

#class SearchForm(forms.Form):
#	search_by = forms.ChoiceField()
#	search_by.label = "Search by"
#	search_by.required = True
#	search_for = forms.CharField()
#	search_for.label = "Search for"
#	search_for.required = True

#def index(request):
#    if request.method == 'POST':
#        form = LoginForm(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect('/ok')
#    else:
#        form = LoginForm()
#
#    return render(request, 'store/index.html', { 'form': form })

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

def search(request):
    state = "Search page"
#	form = SearchForm();
    return render_to_response('store/search.html',
                              {'state': state}, context_instance = RequestContext(request))


def email_send(request):
    this_id = request.GET.get('id', 'NO USER SPECIFIED')
    bookname = request.GET.get('book', 'NO BOOK SPECIFIED')
    reply_email = request.POST.get('reply_email','NO REPLY EMAIL PROVIDED')
    phone = request.POST.get('phone','NO PHONE NUMBER PROVIDED')
    availability = request.POST.get('availability','NO AVAILIBILITY PROVIDED')
    message = request.POST.get('message','NO MESSAGE PROVIDED')
    user = User.objects.get(id=this_id)
    email = user.email
    subject = 'Buchladen: Someone is interested in your book "'+bookname+'"!'
    message = message+"\n\n\nTO REPLY TO THIS USER, USE THE PROVIDED EMAIL: "+reply_email+"\nOR CONTACT THEM AT THIS PHONE NUMBER: "+phone+'\n\nUSER\'S AVAILABILITY: "'+availability+'"'
    #send_mail(subject, message, 'noreply@buchladen.uwinsocr.ca',[email], fail_silently=False);
    return render_to_response('store/email-sent.html', context_instance = RequestContext(request))
        
def isbn(request, isbn_number):
    state = "isbn result page"
    #books = []
    #target = isbn_number

    books = Book.objects.filter(isbn__icontains = isbn_number).order_by('title')

    #for book in Book.objects.all():
    #    if book.isbn == target:
    #        books.append(book)
    #    elif "978"+target == book.isbn:
    #        books.append(book)
    return render_to_response('store/book_list.html',
                              {'state': state, 'book_list': books, 'title_banner': 'Isbn Results'})


def author(request, author_name):
    state = "author result page"

    author = Author.objects.filter(name__icontains = author_name)
    books = Book.objects.filter( authors__in = author).order_by('title')

    books = list(Book.objects.filter( authors = author))
    sort(books, author_name.lower(), "title")

    return render_to_response('store/book_list.html',
                              {'state': state, 'book_list': books, 'title_banner': 'Author Results'})


def title(request, title_name):
    state = "title result page"
    target = title_name.lower()

    books = list(Book.objects.filter(title__icontains = target))
    sort(books, target, "title")

    return render_to_response('store/book_list.html',
                              {'state': state, 'book_list': books, 'title_banner': 'Title Results'})

def sort(books, target, field):
    temp = []
    if field == "title":
        for book in books:
            if target == book.title.lower():
                temp.append(book)
                books.remove(book)

        for i in range(0, len(books)):
            for j in range(i+1, len(books)):
                if books[i].title > books[j].title:
                    books[i], books[j] = books[j], books[i]

    else:
        for book in books:
            for author in book.authors.all():
                if target == author.name.lower():
                    temp.append(book)
                    books.remove(book)

        for i in range(0, len(books)):
            for j in range(i+1, len(books)):
                if books[i].authors[0] > books[j].authors[0]:
                    books[i], books[j] = books[j], books[i]

    if temp:
        for i in range(0, len(temp)):
            for j in range(i+1, len(temp)):
                if temp[i].title > temp[j].title:
                    temp[i], temp[j] = temp[j], temp[i]
        for i in range(0, len(temp)):
            books.insert(0, temp[i])

@json_view
def search_view(request, search_terms):
    print("Searching for: %s" % search_terms)
    results = list(Search(SearchTerms(search_terms)).results())
    print("Returned " + str(results))
    book_serial = BookSerializer()
    return book_serial.list_deflate(results)
