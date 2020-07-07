from django.contrib import admin
from django.urls import path
from testapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook', index, name='webhook'),
]
