from django.forms import ModelForm
from .models import Patient

class PatientForm(ModelForm):
  class Meta:
    model = Patient
    fields = ('gender', 'dateOfBirth', 'country', 'profilePicture')
    
    
