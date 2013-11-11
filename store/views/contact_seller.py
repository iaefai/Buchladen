
from store.forms import ContactForm
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.views.generic import TemplateView

def contact_seller(request):
    user = request.GET.get('id', 'NO_USER_SPECIFIED');
    bookname = request.GET.get('bookname', 'NO_BOOK_SPECIFIED');
    form = ContactForm()
    return render_to_response('store/contact_seller.html',
                              {'user': user, 'bookname':bookname, 'form': form},
                              context_instance = RequestContext(request))

#class ContactSeller(TemplateView):
#    template_name = "store/contact_seller.html"
#
#    def get(self, request, *args, **kwargs):
#

from django.views.generic.edit import FormView

class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/email-sent/"

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)
