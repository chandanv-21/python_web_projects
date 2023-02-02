from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math


# Create your views here.


def index(request):
    # product = Product.objects.all()
    # print(product)
    # n = len(product)
    # nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
    # params = {'no_of_slides': nSlides, 'range': range(1,nSlides), 'product': products}
    # allProds=[[product,range(1,nSlides),nSlides],[product,range(1,nSlides),nSlides]]
    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, myid):
    # Fetch the product using ID.
    product = Product.objects.filter(id=myid)
    print(product)

    return render(request, 'shop/prodview.html', {'product': product[0]})


def cart(request):
    return render(request, 'shop/cart.html')


def checkout(request):
    return HttpResponse('we are at Checkout')
