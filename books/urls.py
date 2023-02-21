from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('lists', list_books, name='list_books'),
]
