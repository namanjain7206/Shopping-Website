from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    p=  Product.objects.all()
    n= len(p)
    nSlides = n//4 + ceil(n/4 - n//4)
    print(nSlides)
    params={'nSlides':nSlides,'range':range(1,nSlides),'product': p,'no_of_product': n }
    return render(request,'Shop/index.html',params)

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