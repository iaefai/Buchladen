from django.conf.urls import patterns, url

from store import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login$', views.RegisterLogin.as_view(), name='register_login'),
    url(r'^logout$', views.Logout.as_view(), name='logout'),
    url(r'^search/(?P<search_terms>.+)', views.search_view, name='search_view'),
    url(r'^recent/(?P<n>[0-9]+)', views.most_recent, name='most_recent'),
    url(r'^contact-seller.+', views.contact_seller, name='contact_seller'),
    url(r'^email-sent/$', views.email_send, name='email_send'),
    url(r'^post-book.+', views.Post.as_view(), name='post_book'),
)
