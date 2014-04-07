from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
  senderID = models.ForeignKey(User, related_name='creator')
  receiverID = models.ForeignKey(User, related_name='target')
  subject = models.TextField()
  chart = models.TextField(null=True, blank=True)
  timeCreated = models.DateTimeField(auto_now_add=True, auto_now=False)
  lastUpdated = models.DateTimeField(auto_now_add=True, auto_now=True)
  
  def __unicode__(self):
    return self.subject
  
  #@classmethod
  #def create(cls, subject):
  #  thread = cls(subject=subject):
  #  return thread

class Message(models.Model):
  thread = models.ForeignKey(Thread)
  senderID = models.ForeignKey(User, related_name='sender')
  receiverID = models.ForeignKey(User, related_name='receiver')
  fromPatient = models.BooleanField()
  timeSent = models.DateTimeField(auto_now_add=True, auto_now=False)
  timeOpened = models.DateTimeField(auto_now_add=False, auto_now=True)
  message = models.TextField()
  
  def __unicode__(self):
    return self.message
  
