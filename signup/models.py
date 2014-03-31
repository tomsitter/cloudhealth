from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# User model provides first and last name, user name, email, and other information
class Patient(models.Model):
  userID = models.OneToOneField(User)
  gender = models.CharField(max_length=1, null=True, blank=True)
  dateOfBirth = models.DateField(null=True, blank=True)
  profilePicture = models.ImageField(upload_to='profile/', null=True, blank=True, default='/home/action/workspace/cloudhealth/static/images/cloud_dialog.png')
  height = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
  weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
  country = CountryField()

class Caregiver(models.Model):
  userID = models.OneToOneField(User)
  profilePicture = models.ImageField(upload_to='profile/', null=True, blank=True, default='/home/action/workspace/cloudhealth/static/images/cloud_dialog.png')
  country = CountryField()