from django.forms import ModelForm
from signup.models import Patient

class PatientForm(ModelForm):
  class Meta:
    model = Patient
    fields = ('gender', 'dateOfBirth', 'country', 'height', 'weight', 'profilePicture')
    #widgets = {
    #        'gender': Select(attrs={'cols': 80, 'rows': 20}),
    #    }