from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PatientForm, DiseaseForm
from .models import Patient, DiseaseList
# Create your views here.
@login_required(login_url='/accounts/login') 
def profile(request):
  
  user = request.user
  try:
    p_instance = Patient.objects.get(userID=user)
  except Patient.DoesNotExist:
    p_instance = None
  profile_form = PatientForm(instance=p_instance, prefix='profile_form')
  
  try:
    d_instance = DiseaseList.objects.filter(user = user)
  except DiseaseList.DoesNotExist:
    d_instance = None
  full_name = request.user.username
  
  if request.method == 'POST':
    if 'profile_submit' in request.POST:
      profile_form = PatientForm(request.POST, prefix='profile_form', instance=p_instance)
      if profile_form.is_valid():
        save_it = profile_form.save(commit=False)
        save_it.userID = request.user
        save_it.save()
        messages.add_message(request, messages.SUCCESS, 'Profile updated successfully!')
        return render_to_response("profile/profile.html",
                                  locals(),
                                  context_instance=RequestContext(request))
    
  return render_to_response("profile/profile.html",
                 locals(),
                 context_instance=RequestContext(request))
