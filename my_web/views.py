from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q


# Create your views here.

def create_order(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        data = request.POST
        order = Order.objects.create(
            customer_name = data['customer_name'],
            count = data['count'],
        )
        product = product
        product.stock -= int(data['count'])
        product.save()
        order.product_id.add(product)
        return redirect('get_products')
    
    return render(request, 'add_orders.html', {"product": product})
    
    
def get_products(request):
    
    query = request.GET.get('q')
    products=Product.objects.all()
    if query:
        products=products.filter(
            product_name__icontains = query
        )
    return render(request, 'show_products.html', {"products":products, 'query':query})



def categories(request):
    categories = Category.objects.all()

    return render(request, 'categories.html', {
        'categories': categories
    })


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'products.html', {'products': products,'categories': categories})


def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})




def home(request):
    return render(request, 'home.html')