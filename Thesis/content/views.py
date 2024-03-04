from django.shortcuts import render, get_object_or_404
from .models import Thesis
from django.core.paginator import Paginator



def index_page(request):
    return render(request, 'landing_page.html')

def show_thesis(request):
    theses_list = Thesis.objects.all()
    paginator = Paginator(theses_list, 3)
    page_number = request.GET.get('page', 1)
    theses = paginator.page(page_number)
    return render(request, 'inner_working/list.html', {'existing_data': theses})


def thesis_search(request):
    query = request.GET.get('q')
    theses = Thesis.objects.all()
    
    if query:
        print("Query:", query)
        theses = theses.filter(keywords__icontains=query)

    return render(request, 'inner_working/list.html', {'theses': theses, 'search_query': query})

def thesis_details(request, year, month, day, thesis):
    thesis = get_object_or_404(Thesis,slug=thesis,published_date__year = year, published_date__month = month, published_date__day = day)
    return render(request,"inner_working/thesis_details.html", {"thesis":thesis})

