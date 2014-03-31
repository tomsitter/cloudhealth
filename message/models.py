from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
  senderID = models.ForeignKey(User, related_name='sender')
  receiverID = models.ForeignKey(User, related_name='receiver')
  fromPatient = models.BooleanField()
  timeSent = models.DateTimeField(auto_now_add=True, auto_now=False)
  timeOpened = models.DateTimeField(auto_now_add=False, auto_now=True)
  message = models.TextField()