from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('catalog/', include('catalog.urls'), name='library'),
    path('checkers/', include('checkers.urls'), name='checkers'),

]

# urlpatterns += [
#     path(r'accounts/', include('django.contrib.auth.urls')),
# ]