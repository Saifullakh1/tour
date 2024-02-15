from django.shortcuts import render
from .models import Review


def review_list(request):
    reviews = Review.objects.all()
    print("reviews", reviews)
    return render(request, 'testimonial.html', {'reviews': reviews})