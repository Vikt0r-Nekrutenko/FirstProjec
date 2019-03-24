from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import apps
from django.shortcuts import redirect
# Create your views here.

def show_name(request):
    return HttpResponse(apps.Application4Config.name)

def foo(request):
    return redirect('redirected/')

def redirected(request):
    return HttpResponse('You were redirected')

def render_html(request):
    _html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
            <h1>Hello vikt0r!</h1>
        </body>
        </html>
    """
    return HttpResponse(_html)

def render_template(request):
    return render(request, 'index.html')

def show_method(request):
    if request.method == 'POST':
        return HttpResponse('Post')
    else:
        return HttpResponse('Get')