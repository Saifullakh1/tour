from django.shortcuts import render
from .models import Tour


def index(request):
    tours = Tour.objects.all()
    return render(request, 'tours/tour_list.html', {'tours': tours})


def tour_detail(request, id):
    tour = Tour.objects.get(id=id)
    return render(request, 'tours/tour_detail.html', {'tour': tour})

