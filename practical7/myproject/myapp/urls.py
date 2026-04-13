from django.urls import path

from . import views
urlpatterns = [
path('', views.home),
]
8. Connect URLs
Open: myproject/urls.py include below code
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('', include('myapp.urls')),
path('admin/', admin.site.urls),
]