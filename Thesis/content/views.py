from django.shortcuts import render, get_object_or_404
from .models import Thesis, Comment
from django.core.paginator import Paginator
from .forms import CommentForm
from django.views.decorators.http import require_POST



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
    comments = thesis.comments.filter(active=True)
    form = CommentForm()
    return render(request,"inner_working/thesis_details.html", {"thesis":thesis,'comments':comments, 'form':form})


@require_POST
def post_comment(request, thesis_id):
    post = get_object_or_404(Thesis,id=thesis_id)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    
    return render(request, 'inner_working/comment.html', {'post':post, 'form':form, 'comment':comment })
