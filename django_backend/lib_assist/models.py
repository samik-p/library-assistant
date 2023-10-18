from django.db import models
from django.utils import timezone

# Create your models here.

class Conversation(models.Model):
    time_started = models.DateTimeField(default=timezone.now)
    last_message_id = models.IntegerField(default=0)
    
class Ticket(models.Model):
    resolved = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    resolved_by = models.CharField(max_length=100)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    
class Message(models.Model):
    sender = models.CharField(max_length=20, default="user")
    content = models.TextField(max_length=200, default="")
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    
    responding_to = models.ForeignKey('self', default=None, on_delete=models.CASCADE, null=True, blank=True)

    time_sent = models.DateTimeField(default=timezone.now)
    
    language = models.CharField(max_length=50, default="eng_Latn")

