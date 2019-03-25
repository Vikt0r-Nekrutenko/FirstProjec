from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    years = [2017, 2018, 2019, 2020, 2021]
    context = {
        'name': 'Vikt0r',
        'lastname': 'Nekrutenko',
        'job_year': years,
        'contact': {
            'nickname': 'grhin0',
            'phone': '380(93)00-16-140',
            'email': 'vikt0r.nekrut@outlook.com',
        },
    }
    return render(request, 'index.html', context)

def condition(request):
    context = {
        'days': [1, 2, 3, 4, 5, 6, 7],
        'current_user': 'admin',
        'day': 3,
        'status': 'online',
        'email': 'fffwww@gmail.com',
    }
    return render(request, 'condition.html', context)