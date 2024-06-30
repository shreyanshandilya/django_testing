# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from myapp.views import ItemList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items/', ItemList.as_view(), name='item-list'),
]
