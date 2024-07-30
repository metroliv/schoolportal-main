# events/forms.py
from django import forms
from .models import Events
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_name', 'description', 'date', 'time', 'location', 'organizer', 'status', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
