# events/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Events
from .forms import EventForm

def event_list(request):
    events = Events.objects.all()
    
    query = request.GET.get('q', '')
    location_filter = request.GET.get('location', '')
    
    if query:
        events = events.filter(event_name__icontains=query)
    if location_filter:
        events = events.filter(location__icontains=location_filter)
    
    from django.core.paginator import Paginator
    paginator = Paginator(events, 10)  # Show 10 events per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'events': page_obj.object_list,
        'page_obj': page_obj,
        'query': query,
        'location_filter': location_filter
    }
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('event-list-results.html', context, request=request)
        return JsonResponse({'html': html})
    
    return render(request, 'event_list.html', context)

def event_detail(request, id):
    event = get_object_or_404(Events, pk=id)
    return render(request, 'event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})
