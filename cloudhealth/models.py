from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User



class Disease(models.Model):
  name = models.CharField(max_length=140, null=False, blank=False)
  generalInfo = models.TextField()


# User model provides first and last name, user name, email, and other information
class Patient(models.Model):
  userID = models.OneToOneField(User)
  gender = models.CharField(max_length=1, null=True, blank=True)
  dateOfBirth = models.DateField(null=True, blank=True)
  profilePicture = models.ImageField()
  height = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
  weight = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
  country = CountryField()
  disease = models.ManyToManyField(Disease)
  
class Caregiver(models.Model):
  userID = models.OneToOneField(User)
  profilePicture = models.DateField()
  country = CountryField()
  
class Message(models.Model):
  senderID = models.ForeignKey(User)
  receiverID = models.ForeignKey(User)
  fromPatient = models.BooleanField()
  timeSent = models.DateTimeField(auto_now_add=True, auto_now=False)
  timeOpened = models.DateTimeField(auto_now_add=False, auto_now=True)
  message = models.TextField()  
  

  
