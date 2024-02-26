from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('DjangoHUDApp.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'DjangoHUDApp.views.handler404'