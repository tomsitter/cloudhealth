from django.forms import ModelForm

Class PatientForm(ModelForm):
  class Meta:
    model = Patient
    fields ('gender', 'dateOfBirth', 'country', 'profilePicture')
    
    
