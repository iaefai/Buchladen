
from django.views.generic.base import View
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'store/index.html'
