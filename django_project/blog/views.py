from django.shortcuts import render


# Create your views here.

posts = [
    {
        'author': 'Ricky Mitchell',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 24, 2022'
    },
    {
        'author': 'Amy Mitchell',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 25, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
