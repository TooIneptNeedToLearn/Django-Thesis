from django.shortcuts import render
from .models import Thesis

def show_thesis(request):
    theses = Thesis.objects.all()
    return render(request, 'list.html', {'theses': theses})

def thesis_search(request):
    if 'q' in request.GET:
        query = request.GET['q']
        theses = Thesis.objects.filter(keywords__icontains=query)
    else:
        theses = Thesis.objects.all()
    return render(request, 'list.html', {'theses': theses})


