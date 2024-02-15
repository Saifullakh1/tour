from django.shortcuts import render
from .models import Tour
from apps.guides.models import Guide


def index(request):
    tours = Tour.objects.all()
    guides = Guide.objects.all()[:4]
    return render(request, 'tours/tour_list.html', {'tours': tours, 'guides': guides})


def tour_detail(request, id):
    tour = Tour.objects.get(id=id)
    return render(request, 'tours/tour_detail.html', {'tour': tour})

