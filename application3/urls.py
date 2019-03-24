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
from typing import List, Any

from django.conf.urls import url
from django.urls import path, include
from . import views

new_patterns = [
    url(r'^comments/$', views.get_comment),
    url(r'^comments/(?P<comment_number>\d+)/$', views.get_comment),
]

action_patterns = [
    path('edit/', views.edit),
    path('delete/', views.delete),
    path('answer/', views.answer),
]

urlpatterns = [
    url(r'^review/page-(?P<page_number>[1-9][\d]{0,})/$', views.get_page),
    url('new_patterns/', include(new_patterns)),
    url(r'product/review/page-(?P<page_number>[1-9][\d]{0,})/', include(action_patterns)),
]

