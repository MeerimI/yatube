from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post

def index(request):
    post_list = Post.objects.order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page':page, 'paginator':paginator}
    )