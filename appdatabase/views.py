from django.shortcuts import render
from django.http import  HttpResponse
from django.views.generic.base import TemplateView
from . import models

# Create your views here.

from django import forms

class MyForm(forms.Form):
    company_name = forms.CharField(label="comp name:", max_length=100)

class List(TemplateView):
    template_name = "template.html"

    context = {
        'humans': list(models.Human.objects.all()),
        '3humansa': models.Human.objects.all()[:3],
        'first_company': models.Human.objects.filter(company="soft_serve"),
        '2000year': models.Human.objects.filter(birth__gte='2000-01-01', birth__lte='2001-12-31'),
        'first_added': models.Human.objects.all()[0],
        'ord_by_desc_date': models.Human.objects.order_by("-birth"),
        'incorrect_name': models.Human.objects.filter(name__regex=r'[\d+?\s+?]').distinct(),
        'form': MyForm(),
    }

    def get(self, request, *args, **kwargs):
        return render(request, 'template.html', self.context)

    def post(self, request):
        q = request.POST['company_name']
        s = models.Human.objects.filter(company__regex=q)

        context = {
            'txt': q,
            'search': s
        }
        return render(request, "response.html", context)