from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lobby.urls'))
]

urlpatterns += [
    path(r'accounts/', include('django.contrib.auth.urls')),
]