"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product/$', views.show),
    url(r'^product/(?P<year>2019)/$', views.show_cur_year),
    url(r'^product/(?P<year>\d{3,4})/$', views.show_year_folder),
    url(r'^product/(?P<year>\d{3,4})/(?P<month>[1-9]|1[0-2])/$', views.show_months_folder),
    url(r'^product/(?P<year>\d{3,4})/(?P<month>[1-9]|1[0-2])/(?P<day>[1-9]|[1-2][0-9]|3[01])/$', views.show_day_folder),
    url(r'^(?P<your_arg>\w+)$', views.show_your_argument),
    url(r'^folder/product(?P<number>[0-9]+)/$', views.get_product),
    url(r'^folder/$', views.get_product),
    url('', views.show_name)
]
