from django.shortcuts import render
from django.template import loader
def index(request):
    return render(request,'personal.html')
def qual(request):
    return render(request,'qual.html')
def extra(request):
    return render(request,'extra.html')
def skill(request):
    return render(request,'skill.html')

# Create your views here.
