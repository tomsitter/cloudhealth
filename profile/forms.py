from django import forms
from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget
from .models import Patient, Caregiver, DiseaseList, DiseaseChoices

#GENDER_CHOICES = ('M', 'F', 'O')
GENDER_CHOICES = (('M', 'Male'),
                  ('F', 'Female'),
                  ('O', 'Other'))

class PatientForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = ('gender', 'dateOfBirth', 'country', 'height', 'weight',)
    widgets = {
            'gender': widgets.Select(choices = GENDER_CHOICES),
            'dateOfBirth': SelectDateWidget(years=range(2014,1910,-1))
            }
    
class DiseaseForm(forms.ModelForm):
  class Meta:
    model = DiseaseList
    fields = ('disease',)
    
  def __init__(self, *args, **kwargs):
    super(DiseaseForm, self).__init__(*args, **kwargs)
    
    self.fields['disease'].widget = forms.CheckboxSelectMultiple()
    self.fields['disease'].queryset = DiseaseChoices.objects.all()
    
class DiseaseChoiceForm(forms.ModelForm):
  class Meta:
    model = DiseaseChoices
    fields = ('fullName',)
    choices = forms.ModelChoiceField(label="Self-care modules", queryset=DiseaseChoices.objects.all(), widget=forms.Select(attrs={'class':'selector'})) 
    #widgets = {
    #           'fullName': forms.Select(attrs={'class': 'select'}),
    #           queryset = DiseaseChoices.objects.all(),
    #           }