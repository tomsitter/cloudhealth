from django.forms import ModelForm
from .models import Message

class MessageForm(ModelForm):
  class Meta:
    model = Message
    fields = ('message',)
    
    def saveMessage(self):
      #save the message to the database
      pass