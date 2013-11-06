from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from django.contrib.auth.models import User, Group

admin.autodiscover()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'Buchladen.views.home', name='home'),
    # url(r'^Buchladen/', include('Buchladen.foo.urls')),
    url(r'^$', include('store.urls', namespace='store')),
    url(r'^index', 'store.views.index'),
    url(r'^login', 'store.views.login_user'),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^booklist', 'store.views.book_list'),
    url(r'^contact-seller', 'store.views.contact_seller'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
