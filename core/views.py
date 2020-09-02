from django.shortcuts import render


def index(request):
    linguagens = ['Python', 'JavaScript', 'Ruby']
    context = {
        'title': 'E-Commerce',
        'linguagens': linguagens,
    }
    return render(request, 'index.html', context)
