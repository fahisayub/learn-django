from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'helloapp/index.html')
def fahiz(request):
    return HttpResponse('Hello Fahiz')
def greetuser(request,name):
    return render(request, 'helloapp/greetuser.html',{"name":name.capitalize()})
# def greet(request,name):
#     return HttpResponse(f"Hello,{name.capitalize()}!")