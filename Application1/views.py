from django.http import HttpResponse

# Create your views here.

def show(request):
    return HttpResponse("Hello, it's Application1")