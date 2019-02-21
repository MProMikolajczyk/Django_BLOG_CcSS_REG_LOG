from django.shortcuts import render
from .models import Post

#budowa danych w databases
posts = [
    {
        'author': 'Marek Mikołajczyk',
        'title': 'Blog Post 1',
        'content': 'Fist post content',
        'date_posted': 'August 27,2018',
    },
{
        'author': 'Kasia Figura',
        'title': 'Blog Post 2',
        'content': 'Secend post content',
        'date_posted': 'August 28,2018',
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title':'About'})