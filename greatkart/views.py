from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def home(request):
    #taking all products and using filter by availabling
    products = Product.objects.all().filter(is_available = True)
    
    context = {
        'products': products,
    }
    
    return render(request, 'home.html', context)


