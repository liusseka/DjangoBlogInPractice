from django.shortcuts import render

posts = [
    {
        'author': 'Julius Charles',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'January 11, 2024'
    },
    {
        'author': 'Kennedy Charles',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'January 12, 2024'
    }
]


def home(requests):
    context = {
        'posts': posts
    }
    return render(requests, 'blog/home.html', context)


def about(requests):
    return render(requests, 'blog/about.html', {'title': 'About'})
