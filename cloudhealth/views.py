#####  Profile View  #####
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


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

@login_required(login_url='/accounts/login')
def logout(request):
  auth.logout(request)
  messages.add_message(request, messages.INFO, "You've logged out. Come by again!")
  return render_to_response("home.html",
                            locals(),
                            context_instance=RequestContext(request))
