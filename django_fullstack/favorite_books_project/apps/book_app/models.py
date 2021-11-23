from django.db import models
from apps.log_and_register_app.models import User
# Create your models here.

class BookManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(post_data['title']) < 2:
            errors["name"] = "Book name should be at least 2 characters"
        if len(post_data['description']) < 10:
            errors["description"] = "Book description should be at least 10 characters"
        return errors
    def update_validator(self, post_data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(post_data['title']) < 2:
            errors["name"] = "Book name should be at least 2 characters"
        if len(post_data['description']) < 10:
            errors["description"] = "Book description should be at least 10 characters"
        return errors
class Book(models.Model):
    title= models.CharField(max_length=255)
    desc= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()
    

    # class User:
    #     liked_books=
    #     books_uploaded=