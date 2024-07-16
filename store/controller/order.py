from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from store.models import Order, OrderItem, Return_req, Product, Seller

def index(request):
    orders=Order.objects.filter(user=request.user).order_by('-order_id')
    context={'orders':orders}
    return render(request, "store/orders/index.html",context)

def vieworder(request, t_id):
    order = Order.objects.filter(order_id=t_id, user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)

    context = {
        'order': order,
        'orderitems': orderitems,
    }
    return render(request, "store/orders/view.html", context)

  
def returnorder(request, t_id):
    order=Order.objects.filter(order_id=t_id).filter(user=request.user).first()
    orderitems=OrderItem.objects.filter(order=order)
    context={'order':order , 'orderitems':orderitems}
    return render(request, "store/orders/return.html",context)
    
 
def request_return(request, item_id):
    order_item = get_object_or_404(OrderItem, order_item_id=item_id)
    user = request.user

    if request.method == 'POST':
        
        existing_return_req = Return_req.objects.filter(order=order_item.order, user=user).first()

        if existing_return_req:
            messages.error(request, "A return request has already been made for this item.")
        else:
            
            return_req = Return_req.objects.create(
                order=order_item.order,
                user=user,
                return_reason=request.POST.get('return_reason', 'Customer request'),  # Get reason from user input
                return_status="Requested",
                return_date=timezone.now()
            )
            messages.success(request, "Return request successfully created.")
            
            
             # Automatically approve the return request and adjust product quantity
            order_item = OrderItem.objects.get(order=return_req.order, user=user)
            product = order_item.product
            product.quantity += 1  # Increase quantity by 1 upon return request
            product.save()

            # Mark order item as returned
            order_item.status = "Returned"
            order_item.save()

            messages.success(request, f"Return request for {order_item.product.name} has been approved automatically.")
        
    return render(request, 'store/index.html')