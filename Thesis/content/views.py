from django.shortcuts import render, get_object_or_404
from .models import Thesis

def show_thesis(request):
    theses = Thesis.objects.all()
    return render(request, 'list.html', {'theses': theses})

def show_thesis_detail(request, thesis_id):
    thesis = get_object_or_404(Thesis, pk=thesis_id)
    return render(request, 'inner_working/thesis_detail.html', {'thesis': thesis})

def thesis_search(request):
    if 'q' in request.GET:
        query = request.GET['q']
        theses = Thesis.objects.filter(keywords__icontains=query)
    else:
        theses = Thesis.objects.all()
    return render(request, 'list.html', {'theses': theses})
