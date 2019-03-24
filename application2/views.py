from django.http import HttpResponse
from . import apps

# Create your views here.

def show(request):
    return HttpResponse('application2/product')

def show_name(request):
    return HttpResponse(apps.Application2Config.name)

def show_cur_year(request, year):
    return HttpResponse('It\'s current year folder')

def show_year_folder(request, year):
    return HttpResponse('It\'s year basic folder')

def show_months_folder(request, year, month):
    return HttpResponse('It\'s months basic folder')

def show_day_folder(request, year, month, day):
    return HttpResponse('It\'s days basic folder')

def show_your_argument(request, your_arg):
    return HttpResponse('Your argument is ' + your_arg)

def get_product(request, number = '1'):
    if number == '1':
        return HttpResponse('First product page')
    else:
        return HttpResponse('product page with number ' + number)

