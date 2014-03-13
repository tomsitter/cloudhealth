from django.db import models
from django_countries.fields import
from django.contrib.auth.models import User

# User model provides first and last name, user name, email, and other information

class Patient(models.Model):

  userID = models.OneToOneField(User)
  gender = models.CharField(max_length=1)
  dateOfBirth = models.DateField()
  profilePicture = models.ImageField()
  height = models.DecimalField(max_digits=5, decimal_places=3)
  weight = model.DecimalFields(max_digits=5, decimal_places=3)
  country = models.CountryField()
  
class Caregiver(models.Model):
  
  userID = models.OnetoOneField(User)
  profilePicture = models.DateField()
  country = models.CountryField()
  
class Message(models.Model):
  
  senderID = models.ForeignKey(User)
  receiverID = models.ForeignKey(User)
  fromPatient = models.BooleanField()
  timeSent = models.DateTime(auto_now_Add=True)
  timeOpened = models.DateTimeField()
  message = models.TextField()
  
class Disease(models.Model):
  
  name = models.CharField(max_length=140)
  generalInfo = models.TextField()
  
  

  
