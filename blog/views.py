from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'title': 'Blog Post 1',
        'content': 'Hello there, this is my first blog',
        'author': 'Andrew Lee',
        'date_posted': 'Feb 15, 2020',
    },
    {
        'title': 'Blog Post 2',
        'content': 'Well fancy seeing you here, this is my second blog',
        'author': 'Brian Park',
        'date_posted': 'Feb 16, 2020',
    }
]


def home(request):
    context = {
        'posts':posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "Andrew's Blog - About Page"}) 