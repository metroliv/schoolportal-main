# events/forms.py
from django import forms
from .models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_name', 'description', 'date', 'time', 'location', 'organizer']
