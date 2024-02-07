from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import random
from .models import Post

def post_view(request, id):
    post = Post.objects.get(id = id)
    context = {"post":post}
    return render(request, "core/post.html", context)

def random_post(request):
    items = list(Post.objects.all())
    random_item = random.choice(items)
    return HttpResponseRedirect(reverse("posts:post",kwargs={"id":random_item.id}))