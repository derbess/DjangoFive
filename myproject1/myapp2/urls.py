from django.urls import path
from .views import create_user, my_view


urlpatterns = [
    path('registr', create_user),
    path('login', my_view)
]