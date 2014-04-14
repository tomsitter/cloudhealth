from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# User model provides first and last name, user name, email, and other information
class Patient(models.Model):
  userID = models.OneToOneField(User)
  gender = models.CharField(max_length=1, null=True, blank=True)
  dateOfBirth = models.DateField("Date of birth", null=True, blank=True)
  profilePicture = models.ImageField("Profile Picture", upload_to='profile/', null=True, blank=True, default='/home/action/workspace/cloudhealth/static/images/cloud_dialog.png')
  height = models.DecimalField("Height (cm)", max_digits=6, decimal_places=1, null=True, blank=True)
  weight = models.DecimalField("Weight (kg)", max_digits=6, decimal_places=1, null=True, blank=True)
  country = CountryField(null=True, blank=True)
  
  def __unicode__(self):
    return self.userID.username

class Caregiver(models.Model):
  userID = models.OneToOneField(User)
  profilePicture = models.ImageField("Profile picture", upload_to='profile/', null=True, blank=True, default='/home/action/workspace/cloudhealth/static/images/cloud_dialog.png')
  country = CountryField(null=True, blank=True)
  
  def __unicode__(self):
    return self.userID.username

class DiseaseChoices(models.Model):
  fullName = models.CharField("Self-care Module", max_length=100, null=False, blank=False, unique=True)
  shortName = models.CharField(max_length=5, null=False, blank=False, unique=True)
  
  def __unicode__(self):
    return self.fullName
  
class DiseaseList(models.Model):
  user = models.ForeignKey(User)
  disease = models.ManyToManyField(DiseaseChoices)
  