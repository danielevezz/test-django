from django.shortcuts import render

from .models import Event


def program(request):
    event_list = Event.objects.all()
    context = {"event_list": event_list}
    return render(request, 'website/program.html', context)


def detail(request, event_id):
    e = Event.objects.get(id=event_id)
    context = {"event": e}
    return render(request, 'website/detail.html', context)
