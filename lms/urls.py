from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render

def index(request):
    context = {'msg':"This is index page"}
    return render(request,'index.html',context)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index,name='index'),
    path('users/',include('users.urls',namespace='users')),
]
