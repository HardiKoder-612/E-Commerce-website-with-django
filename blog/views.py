from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
from math import ceil
# Create your views here.
def index(request):
    allPosts = []
    titposts = Blogpost.objects.values('title', 'id')
    titles = {item['title'] for item in titposts}
    for title in titles:
        post = Blogpost.objects.filter(title=title)
        n = len(post)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allPosts.append([post, range(1, nslides), nslides])
    params = {'allposts': allPosts}
    return render(request,"blog/index.html",params)

def blogpost(request):
    return render(request,"blog/blogpost.html")

