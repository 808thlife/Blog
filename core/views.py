from django.shortcuts import render
from django.core.paginator import Paginator
from posts.models import Post
# Create your views here.

def index(request):
    posts_list = Post.objects.all().order_by('-id')
    paginator = Paginator(posts_list, 5)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {"posts": posts}
    return render(request, "core/index.html", context)

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")