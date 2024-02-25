from django.shortcuts import render
from .models import Thesis

def show_thesis(request):
    theses = Thesis.objects.all()
    return render(request, 'list.html', {'existing_data': theses})

def thesis_search(request):
    query = request.GET.get('q')
    theses = Thesis.objects.all()
    
    if query:
        print("Query:", query)
        theses = theses.filter(keywords__icontains=query)
        print("Executed Query:", theses.query)

    return render(request, 'list.html', {'existing_data': Thesis.objects.all(), 'theses': theses, 'search_query': query})

