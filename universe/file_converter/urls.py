from . import views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', views.index, name='file_converter'),
    re_path(r'^convert/$', views.load_files, name='convert'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


