from django.contrib import admin
from signup.models import Patient, Caregiver, DiseaseChoices, DiseaseList

admin.site.register(Patient)
admin.site.register(Caregiver)
admin.site.register(DiseaseChoices)
admin.site.register(DiseaseList)
