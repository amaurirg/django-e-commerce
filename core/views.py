from django.shortcuts import render


def index(request):
    context = {
        'title': 'E-Commerce',
    }
    return render(request, 'index.html', context)
