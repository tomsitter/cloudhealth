from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
def dashboard(request):
  return render_to_response("dashboard/dashboard.html",
                            {'full_name': request.user.username},
                            context_instance=RequestContext(request))