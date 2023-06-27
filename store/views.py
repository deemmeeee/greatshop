from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    #if category_slug is not None, catalog is filtring by Category
    if category_slug != None:
        # get_object_or_404 используется для получения объекта Category 
        #по заданному slug (полю URL-адреса) или возвращения ошибки 404, 
        #если объект не найден.Если путь не пустой тогда команда ищет этот путь 
        #в классе с моделями CAtegory среди slug моделей
        
        categories = get_object_or_404(Category, slug=category_slug)
        # Product.objects.filter выполняет запрос к модели Product, фильтруя только те объекты,
        #у которых поле category соответствует 
        #выбранной категории (categories) и у которых поле is_available имеет значение True.
        products = Product.objects.filter(category=categories, is_available=True)
        #amount of products
        product_count = products.count()
    else:    
        products = Product.objects.all().filter(is_available = True)
        product_count = products.count()
    context = {
        'products': products,
        #amount of products
        'product_count':product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)