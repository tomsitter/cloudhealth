#####  Message View  ###### 

from django.http import HttpResponseRedirect#,HttpResponse,  Http404 <- can use shortcut
#from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from .forms import MessageForm, ThreadForm
from diabetes.models import BloodSugar
from profile.models import Patient, Caregiver, DiseaseList, DiseaseChoices
from .models import Message, Thread
from profile.forms import DiseaseChoiceForm

@login_required(login_url='/accounts/login')
def messages(request):
  
  user = request.user
  choices = DiseaseChoices.objects.all()
  disease_choice_form = DiseaseChoiceForm()
  chart = None
  #received_threads = Thread.objects.filter(
  #            receiverID = user_id
  #            ).order_by('-lastUpdated')
  
  if request.method == 'POST':
    if 'createmsg-message' in request.POST:
      messageform = MessageForm(request.POST, prefix='createmsg')
      
      if messageform.is_valid():
        obj = messageform.save(commit=False)
        obj.senderID = user
        thread_id = request.POST['createmsg-thread_id']
        #print Thread.objects.get(pk=obj.thread_id)
        thread = Thread.objects.get(pk=thread_id)
        obj.thread = thread
        obj.receiverID = thread.receiverID
        obj.fromPatient = True
        
        #Need to insert the appropriate thread ID before saving!
        obj.save()
    #   threadform = ThreadForm(prefix='createthread')
    elif 'createthread-receiverID' in request.POST:
      threadform = ThreadForm(request.POST, prefix='createthread')

      if threadform.is_valid():
        obj = threadform.save(commit=False)
        obj.senderID = user

        choice = request.POST['disease_module']
        
        if choice == 'dm1':
          obj.chart = "https://plot.ly/~cloudhealth/11"
        elif choice == 'dm2':
          obj.chart = "https://plot.ly/~cloudhealth/11"
        elif choice == 'sad':
          obj.chart = "https://plot.ly/~cloudhealth/18"
        else: 
          obj.chart = None
          
        obj.save()
      else:
        django_messages.add_message(request, django_messages.ERROR, 'Could not create thread. Did you select a recipient and include a subject?')
  #    messageform = MessageForm(prefix='createmsg')
  #else:
  try:
    profile = Patient.objects.get(userID=user)
  except Patient.DoesNotExist:
    profile = None
    
  try:
    disease = DiseaseList.objects.filter(user=user)
  except DiseaseList.DoesNotExist:
    disease = None
  
  previousthreads = Thread.objects.filter(
                      Q(senderID = user) | Q(receiverID=user)
                    ).order_by('-lastUpdated')
  messageform=MessageForm(prefix='createmsg')
  threadform=ThreadForm(prefix='createthread')
  
  return render(request, 'message/message.html',
                 {'previousthreads': previousthreads,
                  'threadform': threadform,
                  'messageform': messageform,
                  'profile': profile,
                  'disease': disease,
                  'disease_choice_form': disease_choice_form,
                  'chart': chart
                  })

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