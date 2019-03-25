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
        }
    }
    return render(request, 'index.html', context)

