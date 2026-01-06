from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView

from .models import Products , Laptop , Computer , GameConsole

# Create your views here.

def index(request):
    return render (request , "trzp/index.html" , {})

def products_page(request, product_slug=None):
    
    if product_slug:
        product = get_object_or_404(Products, slug=product_slug)
        return render(request, "trzp/product_detail.html", {"product": product})

    products = Products.objects.all()
    return render(request, "trzp/products.html", {"products": products})



class LaptopListView(ListView):

    model = Laptop
    # laptop_list.html


class ComputerListView(ListView):

    model = Computer
    # computer_list.html

class GameConsoleListView(ListView):

    model = GameConsole
    # gameconsole_list.html