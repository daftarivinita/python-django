from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.TextField()