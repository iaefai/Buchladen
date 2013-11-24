from django.conf.urls import patterns, url

from store import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login$', views.RegisterLogin.as_view(), name='register_login'),
    url(r'^logout$', views.Logout.as_view(), name='logout'),
    url(r'^search/(?P<search_terms>.+)', views.search_view, name='search_view'),
    #url(r'^login$', views.login_user, name='login_user'),
    #url(r'^contact$', views.ContactView.as_view(), name='contact'),
    url(r'^contact-seller.+', views.contact_seller, name='contact_seller'),
    #url(r'^search/$', views.search, name='search'),
    #url(r'^search/isbn/(?P<isbn_number>[^/]+)$', views.isbn, name='isbn'),
    #url(r'^search/author/(?P<author_name>[^/]+)', views.author, name='author'),
    #url(r'^search/title/(?P<title_name>[^/]+)', views.title, name='title'),
    url(r'^email-sent/$', views.email_send, name='email_send'),
    url(r'^post-book.+', views.post_book, name='post_book'),
    # ex: /polls/5/
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
