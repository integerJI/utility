# app/view.py
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def category(request):
    return render(request, 'category.html')

def check(request):
    
    sample = request.POST['sample'].split('\r\n')
    check = request.POST['check'].split('\r\n')

    print(sample)
    print(check)
    return render(request, 'category.html')
