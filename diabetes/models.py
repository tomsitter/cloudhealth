from django.db import models
from django.contrib.auth.models import User

# Create your models here.
  
class BloodSugar(models.Model):
  userID = models.ForeignKey(User)
  time = models.DateTimeField(auto_now=True)
  blood_glucose = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
  bg_chart = models.TextField(null=True, blank=True)