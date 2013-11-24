from django.http import HttpResponse

from django.views.generic.base import View
from django.template.response import SimpleTemplateResponse
from django.contrib.auth import authenticate, login, logout

from django.template.response import TemplateResponse

#class RegisterLogin(TemplateView):
#    template_name = 'store/register_login.html'
#    http_method_names = ['get', 'post']
#
#    def put(self, request, *args, **kwargs):
#        return HttpResponse("You tried to login!")

class RegisterLogin(View):
    getTemplate = SimpleTemplateResponse('store/register_login.html')
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        return RegisterLogin.getTemplate.render()

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("redirect")
            else:
                return HttpResponse("Disabled account")
        else:
            return HttpResponse("Invalid login")


class Logout(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponse("logged out")

class Register(View):
    def post(self, request, *args, **kwargs):
        pass