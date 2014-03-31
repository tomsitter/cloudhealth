from django.http import HttpResponseRedirect#,HttpResponse,  Http404 <- can use shortcut
#from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from message.models import Message

class IndexView(generic.ListView):
  template_name = 'message/message.html'
  #Generic name would just be poll_list
  context_object_name = 'latest_message_list'
  
  def get_queryset(self):
    """Return the last five messages. (not including messages to be sent in the future)"""
    return Message.objects.filter(
      timeSent__lte=timezone.now()
    ).order_by('-timeSent')[:5]
