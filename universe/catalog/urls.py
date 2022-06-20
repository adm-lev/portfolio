from . import views
from django.views.static import serve
from django.urls import path, include, re_path


urlpatterns = [
    re_path(r'^$', views.index, name='library'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]


urlpatterns += [
    path(r'accounts/', include('django.contrib.auth.urls')),
]




