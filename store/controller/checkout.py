from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from store.models import Address, Cart, Order, OrderItem, Product , Payment, Shipping , Return_req, Seller
from django.contrib import messages
from django.utils import timezone

from django.db import transaction
import uuid
from django.http.response import JsonResponse 
from django.http import HttpResponse

import random
import string


# def product_detail_view(request, category_slug, product_slug):
#     product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
#     seller = get_object_or_404(Seller, product=product)

#     context = {
#         'products': product,
#         'seller': seller,
#     }

#     return render(request, 'store/product_detail.html', context)


# client = razorpay.Client(auth=("rzp_test_BzE6HdexQFvWsD", "gKjci1mPILUp4ini3BTIX8po"))
@login_required(login_url='loginpage')
def place_order(request):
    if request.method == 'POST':
       
        user = request.user
        payment_method = request.POST.get('payment_method')
        cart_items = Cart.objects.filter(user=user)
        total_amount = sum(item.product.selling_price * item.quantity for item in cart_items)

        # Check if there are any entered addresses by the user
        entered_addresses = Address.objects.filter(user=user).exists()

        if not entered_addresses:
            messages.error(request, "Please add an address before placing an order.")
            return redirect('checkout')

        # Find the default address or any address if default is not set
        shipping_address = Address.objects.filter(user=user, is_default=True).first()

        if not shipping_address:
            messages.warning(request, "No default address found. Please select or add an address.")
            return redirect('checkout')

        if not payment_method:
            payment_method = "Cash on Delivery"
        if payment_method == "Razorpay":
            payment_method = "Razorpay"

        try:
            with transaction.atomic():
                # Create an order without campaign
                order = Order.objects.create(
                    user=user,
                    total_amount=total_amount,
                    status="Placed",
                    payment_method=payment_method,
                    shipping_method="Standard",
                    shipping_address=shipping_address,
                    billing_address=shipping_address,
                )
                

                # Create order items and reduce the product quantity
                for item in cart_items:
                    product = item.product

                    # Check if product quantity is sufficient
                    if product.quantity < item.quantity:
                        messages.warning(request, f"Insufficient quantity for {product.name}. Please update your cart.")
                        return redirect('checkout')

                    OrderItem.objects.create(
                        order=order,
                        user=user,
                        product=product,
                        status="Placed",
                        payment_method=payment_method,
                        shipping_method="Standard",
                        shipping_address=shipping_address,
                        billing_address=shipping_address,
                        delivery_status="Pending",
                    )

                    # Reduce product quantity
                    product.quantity -= item.quantity
                    product.save()

                # Generate a random transaction ID
                transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
                
                
                if payment_method == "Razorpay":
                    payment_status = "Completed"
                else:
                    payment_status = "Pending"

                # Create a payment record
                Payment.objects.create(
                    order=order,
                    payment_date=timezone.now(),
                    amount=total_amount,
                    payment_method=payment_method,
                    payment_status=payment_status,
                    transaction_id=transaction_id,
                    authorization_code="NIL",
                    currency="Rs",
                    payment_gateway_response="NIL",
                    payment_notes="order placed" 
                )
                
# f"Card Numo" if payment_method == "Cash on Delivery" else "razorpay"
                # Calculate shipping dates
                shipping_date = timezone.now() + timezone.timedelta(days=1)
                estimated_delivery_date = shipping_date + timezone.timedelta(days=random.randint(2, 4))
                actual_delivery_date = estimated_delivery_date  # For simplicity, actual delivery date is same as estimated

                # Determine shipping cost
                shipping_cost = 0 if total_amount >= 4000 else random.uniform(20, 50)

                # Create a shipping record
                Shipping.objects.create(
                    order=order,
                    shipping_date=shipping_date,
                    estimated_delivery_date=estimated_delivery_date,
                    actual_delivery_date=actual_delivery_date,
                    carrier_name="Default Carrier",
                    tracking_number=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                    shipping_cost=shipping_cost,
                    shipping_method="Standard",
                    shipping_address_id=shipping_address,
                    user_id=user
                )

                # Clear the cart
                cart_items.delete()

                if payment_method == "Razorpay":
                    return JsonResponse({'status': "Order placed successfully!"}, status=200)
                else:
                    messages.success(request, "Order placed successfully!")
                    return redirect('home')

        except Exception as e:
            messages.error(request, f"Error placing order: {str(e)}")
            return redirect('checkout')

    return redirect('checkout')







@login_required(login_url='loginpage')
def checkout(request):
    user = request.user
    addresses = Address.objects.filter(user=user)
    cartitems = Cart.objects.filter(user=user)
    total_price = sum(item.product.selling_price * item.quantity for item in cartitems)
    context = {
        'addresses': addresses,
        'cartitems': cartitems,
        'total_price': total_price,
    }
    return render(request, 'store/checkout.html', context)

@login_required(login_url='loginpage')
def add_address(request):
    if request.method == 'POST':
        street_address = request.POST['street_address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        postal_code = request.POST['postal_code']
        phone_number = request.POST.get('phone_number')
        contact_name = request.POST.get('contact_name')
        company_name = request.POST.get('company_name')
        apartment_number = request.POST.get('apartment_number')
        building_name = request.POST.get('building_name')
        floor_number = request.POST.get('floor_number')
        gate_code = request.POST.get('gate_code')
        delivery_instructions = request.POST.get('delivery_instructions')
        address_type = request.POST.get('address_type')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        is_default = request.POST.get('is_default') == 'on'
        label = request.POST.get('label', 'home')

        address = Address.objects.create(
            user=request.user,
            street_address=street_address,
            city=city,
            state=state,
            country=country,
            postal_code=postal_code,
            phone_number=phone_number,
            contact_name=contact_name,
            company_name=company_name,
            apartment_number=apartment_number,
            building_name=building_name,
            floor_number=floor_number,
            gate_code=gate_code,
            delivery_instructions=delivery_instructions,
            address_type=address_type,
            latitude=latitude,
            longitude=longitude,
            is_default=is_default,
            label=label
        )
        return redirect('checkout')
    return render(request, 'store/checkout.html')



@login_required(login_url='loginpage')
def edit_address(request, address_id):
    address = get_object_or_404(Address, id=address_id, user=request.user)
    if request.method == 'POST':
        address.street_address = request.POST['street_address']
        address.city = request.POST['city']
        address.state = request.POST['state']
        address.country = request.POST['country']
        address.postal_code = request.POST['postal_code']
        address.phone_number = request.POST.get('phone_number')
        address.contact_name = request.POST.get('contact_name')
        address.company_name = request.POST.get('company_name')
        address.apartment_number = request.POST.get('apartment_number')
        address.building_name = request.POST.get('building_name')
        address.floor_number = request.POST.get('floor_number')
        address.gate_code = request.POST.get('gate_code')
        address.delivery_instructions = request.POST.get('delivery_instructions')
        address.address_type = request.POST.get('address_type')
        address.latitude = request.POST.get('latitude')
        address.longitude = request.POST.get('longitude')
        address.is_default = request.POST.get('is_default') == 'on'
        address.label = request.POST.get('label', 'home')
        address.save()
        return redirect('checkout')
    context = {'address': address}
    return render(request, 'store/edit_address.html', context)



@login_required(login_url='loginpage')
def razorpaycheck(request):
    user = request.user
    
    cartitems = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.selling_price * item.quantity for item in cartitems)
   
    return JsonResponse({
        'total_price': total_price
    })
    
    
    
@login_required
def get_address_data(request):
    user = request.user
    address = Address.objects.filter(user=user).first()
    address_data = {
        'contact_name': address.contact_name,
        'street_address': address.street_address,
        'phone_number': address.phone_number,
        'postal_code': address.postal_code,
        'city': address.city,
        'state': address.state,
        'country': address.country,
    }
    return JsonResponse(address_data)



def orders(request):
    return HttpResponse("My orders page")





