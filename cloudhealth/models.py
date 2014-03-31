from django.db import models
  
class Disease(models.Model):
  name = models.CharField(max_length=140, null=False, blank=False)
  generalInfo = models.TextField()
  

  
