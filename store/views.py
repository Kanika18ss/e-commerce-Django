from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def home(request):
    trending_products = Product.objects.filter(trending=True)
    context = {
        'trending_products': trending_products
    }
    return render(request,"store/index.html",context)

def collections(request):
    category= Category.objects.filter(status=0)
    context= {'category' :category}
    return render(request,"store/collections.html",context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products=Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={'products': products, 'category' : category}
        return render(request,"store/products/index.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')
    
  
def productview(request, cate_slug, prod_slug):
    if Category.objects.filter(slug=cate_slug, status=0).exists():
        if Product.objects.filter(slug=prod_slug, status=0).exists():
            product = Product.objects.filter(slug=prod_slug, status=0).first()
            try:
                seller = Seller.objects.get(product=product)
            except Seller.DoesNotExist:
                seller = None
            context = {'product': product, 'seller': seller}
        else:
            messages.error(request, "No such product found")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    
    return render(request, "store/products/view.html", context)



