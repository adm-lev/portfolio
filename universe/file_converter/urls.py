from . import views
from django.urls import path, include, re_path


urlpatterns = [
    re_path(r'^$', views.index, name='file_converter'),
    re_path(r'^convert/$', views.load_files, name='convert'),

]
