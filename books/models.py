from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=64)
    birth_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='author_category')
    status = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=64)
    page_number = models.PositiveSmallIntegerField(default=10)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, related_name='author_books')
    is_publish = models.BooleanField(default=True)
    # TODo image
    status = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
