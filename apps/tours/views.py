from django.shortcuts import render
from .models import Tour


def index(request):
    tours = Tour.objects.all()
    return render(request, 'tours/tour_list.html', {'tours': tours})
