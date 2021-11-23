from django.db import models
from datetime import date
today_date = date.today()

# Create your models here.
class TvManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Title field should be at least 2 characters'
        for show in Tvshow.objects.all():
            if show.title == postData['title']:
                errors['duplictaes'] = "That Show already exists"
        if len(postData['description']) < 5:
            errors["description"] = "Show description should be at least 5 characters"
        if len(postData['network']) < 4:
            errors["network"] = "Blog network should be at least 4characters"
        if len(postData['release_date']) < 1:
            errors['release_date'] = "Please Provide an date and Thank you for your Business"
        elif str(today_date) < postData['release_date']:
            errors['release_date_future'] = "That year seams to be in future"    
        
        return errors
    def update_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Title field should be at least 2 characters'
        
        if len(postData['description']) < 5:
            errors["description"] = "Show description should be at least 5 characters"
        if len(postData['network']) < 4:
            errors["network"] = "Blog network should be at least 4characters"
        if len(postData['release_date']) < 1:
            errors['release_date'] = "Please Provide an date and Thank you for your Business"
        elif str(today_date) < postData['release_date']:
            errors['release_date_future'] = "That year seams to be in future"    
        
        return errors




        
    
class Tvshow(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    network = models.TextField()
    objects = TvManager() 
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


