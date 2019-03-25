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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Application1/', include('Application1.urls')),
    path('application1/', include('application1.urls')),
    path('application2/', include('application2.urls')),
    path('application3/', include('application3.urls')),
    path('application4/', include('application4.urls')),
    path('application5/', include('application5.urls')),
    path('admin/', admin.site.urls),
]
