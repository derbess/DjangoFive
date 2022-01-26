from django.contrib import admin
from django.urls import path, include
from .views import get_list_categories

urlpatterns = [
    path('categories', get_list_categories, name="get_list_categories")
]
