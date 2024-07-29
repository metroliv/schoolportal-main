# events/views.py
from django.shortcuts import render, redirect
from .models import Events
from .forms import EventForm

def event_list(request):
    events = Events.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Correct namespaced URL
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})
