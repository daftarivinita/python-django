from django.db import models
from apps.log_and_register_app.models import User
from datetime import date
todays_date = date.today()
year = todays_date.year
class AuthorManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
# add keys and values to errors dictionary for each invalid field
        if len(post_data['author'])<2 and len(post_data['new_author'])<2:
            errors['author']= "Author name is a required field"
        return errors
        
#objects = BlogManager()    # add this line inside class for which you are this this method
# Create your models here.
class Author(models.Model):
    name= models.CharField(max_length=255)
    
    #written_by= models.ForeignKey(Book, related_name="writer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()
    #books

class BookManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
# add keys and values to errors dictionary for each invalid field
        if len(post_data['title'])<2:
            errors['title']= "title is a required field"
    
        for book in Book.objects.all():
            if Book.title == post_data['title']:
                errors['duplictaes'] = "That Book already exists"
        return errors
class Book(models.Model):
    title= models.CharField(max_length=255)
    author= models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    
    #reviews
class ReviewManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
# add keys and values to errors dictionary for each invalid field
        if len(post_data['review'])<2:
            errors['content']= "review is a required field"
        if int(post_data['rating']) < 1 or int(post_data['rating']) > 5:
            errors['rating'] = 'Review should be 1 to 5 stars.'
    
        
        return errors


class Review(models.Model):
    content= models.TextField()
    rating = models.IntegerField()
    book= models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    reviewed_by= models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
    
    
        