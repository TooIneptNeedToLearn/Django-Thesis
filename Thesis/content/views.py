from django.shortcuts import render, get_object_or_404
from .models import Thesis
from django.core.paginator import Paginator



def index_page(request):
    return render(request, 'landing_page.html')

def show_thesis(request):
    theses = Thesis.objects.all()
    return render(request, 'inner_working/list.html', {'existing_data': theses})


def thesis_search(request):
    query = request.GET.get('q')
    theses = Thesis.objects.all()
    
    if query:
        print("Query:", query)
        theses = theses.filter(keywords__icontains=query)

    return render(request, 'inner_working/list.html', {'theses': theses, 'search_query': query})

def thesis_details(request, id):
    thesis = get_object_or_404(Thesis, pk=id)

    return render(request,"inner_working/thesis_details.html", {"thesis":thesis})

