from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import PatientForm
from signup.models import Patient
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

@login_required(login_url='/accounts/login')
def profile(request):
  
  try:
    instance = Patient.objects.get(userID=request.user)
  except Patient.DoesNotExist:
    instance = None
    
  form=PatientForm(request.POST or None, instance=instance)
  
  if form.is_valid():
    save_it = form.save(commit=False)
    #save_it.userID = request.user
    save_it.save()
    
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

def logout(requst):
  auth.logout(request)
  return render_to_response('logout.html')
