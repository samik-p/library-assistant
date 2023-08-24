from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField(max_length=200)
    
    
    