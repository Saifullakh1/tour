from django.shortcuts import render
from .models import Guide


def list_guide(request):
    guides = Guide.objects.all()
    return render(request, 'guides/list.html', {'guides': guides})
