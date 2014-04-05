from django.http import HttpResponseRedirect#,HttpResponse,  Http404 <- can use shortcut
#from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import generic
from django.utils import timezone
from .forms import MessageForm
from .models import Message

@login_required(login_url='/accounts/login')
def messages(request):
  
  form=MessageForm(request.POST or None)
  
  messages = Message.objects.filter(
               timeSent__lte=timezone.now()
             ).order_by('-timeSent')[:5]
  
  if form.is_valid():
    save_it = form.save(commit=False)
    save_it.save()
    messages = Message.objects.filter(
      timeSent__lte=timezone.now()
    ).order_by('-timeSent')[:5]
    

  
  return render_to_response('message/message.html',
                 {'messages': messages,
                  'form': form})

'''
class MessageView(generic.ListView):
  template_name = 'message/message.html'
  #Generic name would just be poll_list
  context_object_name = 'latest_message_list'
  #form=MessageForm(request.POST or None)
  
  def get_queryset(self):
    """Return the last five messages. (not including messages to be sent in the future)"""
    return Message.objects.filter(
      timeSent__lte=timezone.now()
    ).order_by('-timeSent')[:5]
'''