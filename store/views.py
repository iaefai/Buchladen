from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from polls.models import Poll, Choice
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic

from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response


from django import forms

class IndexView(generic.ListView):
    template_name = 'store/index.html'
    #context_object_name = 'latest_poll_list'

    def get_queryset(self):
    #    """Return the last five published polls."""
    #    return Poll.objects.order_by('-pub_date')[:5]
        return []

class LoginForm(forms.Form):
    username = forms.EmailField()
    username.label = "e-mail"
    username.required = True
    password = forms.PasswordInput()

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

