from django.contrib import admin
from .models import *


class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_publish')
    list_filter = ('status', 'is_publish')


class AdminAuthor(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('status',)


admin.site.register(Book, AdminBook)
admin.site.register(Author, AdminAuthor)
