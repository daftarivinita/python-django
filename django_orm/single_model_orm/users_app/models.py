from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(unique = True,max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# python manage.py makemigrations
# python manage.py migrate
#
def __str__(self):
    return '{} {}' .format(self.first_name, self.last_name)

# the __str__ function creates a human readable name for the entry. This will be useful when we use the shell and when we use  Django admin functionality.
