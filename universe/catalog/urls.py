from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path


urlpatterns = [

    re_path(r'^$', views.index, name='library'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    # re_path(r'special/^$', views.reading, name='book-text'),
    re_path(r'^special/(?P<pk>\d+)$', views.reading, name='special'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




