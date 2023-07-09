from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem

from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.db.models import Q


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
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        #amount of products
        product_count = products.count()
    else:    
        products = Product.objects.all().filter(is_available = True).order_by('id')
        # 6 - amount fo products on 1 page
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products': paged_products,
        #amount of products
        'product_count':product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
        'in_cart' : in_cart,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        "products" : products,
        "product_count" : product_count,
    }
    
    return render(request, 'store/store.html', context)
