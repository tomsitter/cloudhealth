#####  Profile View  #####

from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import PatientForm, DiseaseForm
from signup.models import Patient, DiseaseList
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

@login_required(login_url='/accounts/login')
def profile(request):
  
  user = request.user
  try:
    p_instance = Patient.objects.get(userID=user)
  except Patient.DoesNotExist:
    p_instance = None
    
    
  try:
    d_instance = DiseaseList.objects.filter(user = user)
  except DiseaseList.DoesNotExist:
    d_instance = None 
  #form=PatientForm(request.POST or None, instance=p_instance)
  #disease_form = DiseaseForm()
  full_name = request.user.username
  
  if request.method == 'POST':
    print request.POST
    if 'disease_submit' in request.POST:
      disease_form = DiseaseForm(request.POST, prefix='disease_form')
      if disease_form.is_valid():     
        save_it = disease_form.save(commit=False)
        save_it.user = user
        save_it.save()
        #messages.add_message(request, messages.SUCCESS, 'Disease list updated successfully!')
        #return render_to_response("profile.html",
        #                          locals(),
        #                          context_instance=RequestContext(request))
    elif 'profile_submit' in request.POST:
      profile_form = PatientForm(request.POST, prefix='profile_form', instance=p_instance)
      if profile_form.is_valid():
        save_it = profile_form.save(commit=False)
        save_it.userID = request.user
        save_it.save()
        messages.add_message(request, messages.SUCCESS, 'Profile updated successfully!')
        #return render_to_response("profile.html",
        #                          locals(),
        #                          context_instance=RequestContext(request))
  #else:
  #  form = PatientForm(instance = p_instance)
  #  disease_form = DiseaseForm()

  form = PatientForm(instance=p_instance, prefix='profile_form')
    
  disease_form = DiseaseForm(prefix='disease_form')
  
  #print form
    
  return render_to_response("profile.html",
                 locals(),
                 context_instance=RequestContext(request))


def login(request):
  username = request.POST['username']
  password = request.POST['password']
  
  user = authenticate(username=username, password=password)
  if user is not None:
    if user.is_active:
      login(request, user)
      return HttpResponseRedirect('/dashboard')
    else:
      return HttpResponseRedirect('/accounts/login_error')
  else:
    pass# return a failed login message

@login_required(login_url='/accounts/login')
def dashboard(request):
  return render_to_response('dashboard.html',
                            {'full_name': request.user.username})

def login_error(request):
  return render_to_response('login_error.html')

def logout(request):
  auth.logout(request)
  messages.add_message(request, messages.INFO, "You've logged out. Come by again!")
  return render_to_response("home.html",
                            locals(),
                            context_instance=RequestContext(request))
