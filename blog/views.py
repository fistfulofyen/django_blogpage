from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
post = [
    {
        'author' : 'Mike Zhang',
        'title' : 'First Blog',
        'content' : 'First post content',
        'date_posted' : 'October 10, 2024'
    },
    {
        'author' : 'Emily Johnson',
        'title' : 'Adventures in Tech',
        'content' : 'Exploring new technology trends.',
        'date_posted' : 'October 11, 2024'
    },
    {
        'author' : 'Sarah Lee',
        'title' : 'Health and Wellness',
        'content' : 'Tips for staying healthy while working from home.',
        'date_posted' : 'October 9, 2024'
    },
    {
        'author' : 'David Brown',
        'title' : 'Travel Diaries',
        'content' : 'My recent trip to the mountains.',
        'date_posted' : 'October 8, 2024'
    },
    {
        'author' : 'Anna Roberts',
        'title' : 'Photography Basics',
        'content' : 'A beginner’s guide to photography.',
        'date_posted' : 'October 7, 2024'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})

# from django_blog.urls -> blog.usls -> blog.views 
def test(request):
    return HttpResponse('<h1>Test</h1>')