from django.shortcuts import render
from django.http import HttpResponse
from .models import  Post
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'postss':Post.objects.all()
    }
    return render(request,'blog/home.html',context)



def test(request):
    return HttpResponse("blog test")


def about(request):
    return render(request,'blog/about.html',{'title':'about'})
# Create your views here.
