from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'Shop/index.html')

def contact(request):
    return HttpResponse(" contact ")
def productview(request):
    return HttpResponse(" productview ")
def checkout(request):
    return HttpResponse(" checkout ")
def search(request):
    return HttpResponse(" search ")
def tracker(request):
    return HttpResponse(" tracker ")
def about(request):
    return render(request,'Shop/about.html')