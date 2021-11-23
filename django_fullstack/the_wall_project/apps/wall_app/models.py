from django.db import models
from apps.log_and_register_app.models import User


# Create your models here
class Message(models.Model):
    content= models.CharField(max_length=255)
    posted_by= models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    content= models.CharField(max_length=255)
    commented_by= models.ForeignKey(User, related_name="user_comment", on_delete=models.CASCADE)
    on_message=models.ForeignKey(Message, related_name="message_comment", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    