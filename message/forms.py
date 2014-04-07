from django.forms import ModelForm
from django import forms
from .models import Message, Thread

class MessageForm(ModelForm):
  #message = forms.CharField(widget=forms.Textarea(attrs={'cols': 500, 'rows': 5}))
  class Meta:
    model = Message
    fields = ('message',)
    
    def saveMessage(self):
      #save the message to the database
      pass
    
class ThreadForm(ModelForm):
  class Meta:
    model = Thread
    fields = ('receiverID', 'subject',)