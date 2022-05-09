from django.shortcuts import render
#from django.http import HttpResponse -был нужен для проверки

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def personal(request):
    return render(request, 'main/personal.html')

def library(request):
    return render(request, 'main/library.html')

def creation(request):
    return render(request, 'main/creation.html')

def creation_test(request):
    return render(request, 'main/creation_test.html')