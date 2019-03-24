from django.http import HttpResponse

# Create your views here.

def get_page(request, page_number):
    return HttpResponse('You are reading reviews page '+ page_number)

def get_comment(request, comment_number = 1):
    if comment_number == 1:
        return HttpResponse('First comment')
    else:
        return HttpResponse('Your comment has number ' + comment_number)

def edit(request, page_number):
    return HttpResponse('You are editing page ' + page_number)

def delete(request, page_number):
    return HttpResponse('You are deleting page ' + page_number)

def answer(request, page_number):
    return HttpResponse('You are discussing page ' + page_number)