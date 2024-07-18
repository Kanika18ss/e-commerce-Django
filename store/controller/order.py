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
        if order_item.order.status == 'Canceled':
            messages.error(request, "Return request cannot be made for a canceled order.")
            return redirect('myorders')

        if order_item.return_requested:
            messages.error(request, "A return request has already been made for this item.")
        else:
            return_req = Return_req.objects.create(
                order=order_item.order,
                user=user,
                return_reason=request.POST.get('return_reason', 'Customer request'),
                return_status="Requested",
                return_date=timezone.now()
            )

            order_item.return_requested = True
            order_item.save()

            product = order_item.product
            product.quantity += 1  # Increase product quantity upon return request
            product.save()

            order_item.status = "Returned"
            order_item.save()

            messages.success(request, f"Return request for {order_item.product.name} has been approved automatically.")

    return render(request, 'store/index.html')




def cancel_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.status == 'Canceled':
        messages.info(request, 'This order is already canceled.')
        return redirect('myorders')

    # Check if return requests exist for any order items
    order_items = OrderItem.objects.filter(order=order)
    for item in order_items:
        if item.return_requested:
            messages.error(request, "Cancellation not allowed. Return request exists for one or more items.")
            return redirect('myorders')

    # Check cancellation deadline (2 days after order date)
    cancellation_deadline = order.order_date + timezone.timedelta(days=2)
    if timezone.now() > cancellation_deadline:
        messages.error(request, 'Cancellation period has expired.')
        return redirect('myorders')

    # Update product quantities and cancel the order
    for item in order_items:
        product = item.product
        product.quantity += item.quantity
        product.save()

    order.status = 'Canceled'
    order.save()

    messages.success(request, 'Your order has been canceled.')
    return redirect('myorders')