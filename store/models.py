from django.db import models
import datetime
import os
from django.contrib.auth.models import User

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):
    slug = models.CharField(max_length=150, default="")
    name = models.CharField(max_length=150, default="")
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, default="")
    status = models.BooleanField(default=False, help_text="0-default, 1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default, 1-Trending")
    meta_title = models.CharField(max_length=150, default="")
    meta_keywords = models.CharField(max_length=150, default="")
    meta_description = models.TextField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, default="")
    name = models.CharField(max_length=150, default="")
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    small_description = models.CharField(max_length=250, default="")
    quantity = models.IntegerField(default=0)
    description = models.TextField(max_length=500, default="")
    original_price = models.FloatField(default=0.0)
    selling_price = models.FloatField(default=0.0)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    tag = models.CharField(max_length=150, default="")
    meta_title = models.CharField(max_length=150, default="")
    meta_keywords = models.CharField(max_length=150, default="")
    meta_description = models.TextField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)
    label = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    contact_name = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    apartment_number = models.CharField(max_length=50, null=True, blank=True)
    building_name = models.CharField(max_length=100, null=True, blank=True)
    floor_number = models.CharField(max_length=50, null=True, blank=True)
    gate_code = models.CharField(max_length=50, null=True, blank=True)
    delivery_instructions = models.TextField(null=True, blank=True)
    address_type = models.CharField(max_length=50, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.contact_name},{self.street_address}, {self.city}, {self.state}, {self.postal_code}, {self.country}'

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart {self.id} for {self.user.username}'

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Wishlist {self.id} for {self.user.username}'

class Campaign(models.Model):
    campaign_name = models.CharField(max_length=255, default="")
    duration = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.campaign_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(max_length=100, default='pending')
    payment_method = models.CharField(max_length=100, default='COD')
    shipping_method = models.CharField(max_length=100, default='standard')
    shipping_address = models.ForeignKey(Address, related_name='shipping_orders', on_delete=models.CASCADE)
    billing_address = models.ForeignKey(Address, related_name='billing_orders', on_delete=models.CASCADE)
    return_requested = models.BooleanField(default=False)
    return_approved = models.BooleanField(default=False)
    return_rejected = models.BooleanField(default=False)
    refund_processed = models.BooleanField(default=False)
    refund_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Order {self.order_id}'

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    status = models.CharField(max_length=100, default='pending')
    payment_method = models.CharField(max_length=100, default='COD')
    shipping_method = models.CharField(max_length=100, default='standard')
    shipping_address = models.ForeignKey(Address, related_name='shipping_order_items', on_delete=models.RESTRICT)
    billing_address = models.ForeignKey(Address, related_name='billing_order_items', on_delete=models.RESTRICT)
    delivery_status = models.CharField(max_length=100, default='pending')
    delivery_date = models.DateField(null=True, blank=True)
    cancellation_reason = models.CharField(max_length=255, null=True, blank=True)
    cancellation_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)

    def __str__(self):
        return f'OrderItem {self.order_item_id} of Order {self.order.order_id}'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order= models.ForeignKey(Order, on_delete=models.RESTRICT)
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=255)
    authorization_code = models.CharField(max_length=255)
    currency = models.CharField(max_length=3)
    payment_gateway_response = models.TextField()
    payment_notes = models.TextField()
    
    def __str__(self):
        return f'Payment {self.payment_id},{self.payment_method}'
    
class Shipping(models.Model):
    shipping_id = models.AutoField(primary_key=True)
    order=models.ForeignKey(Order, on_delete=models.RESTRICT)
    shipping_date = models.DateTimeField()
    estimated_delivery_date = models.DateTimeField()
    actual_delivery_date = models.DateTimeField(null=True, blank=True)
    carrier_name = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=255)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_method = models.CharField(max_length=255)
    shipping_address_id = models.ForeignKey(Address, on_delete=models.RESTRICT)
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return f'Shipping {self.shipping_id},{self.tracking_number},{self.user_id}'
    
    
    
class Return_req(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    return_reason = models.TextField()
    return_status = models.CharField(max_length=100)
    return_date = models.DateTimeField(auto_now_add=True)
    resolution_notes = models.TextField(blank=True, null=True)
    resolution_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Return_req {self.id} for Order {self.order.id}"


    
class Seller(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    
    def __str__(self):
        return self.company_name
    
   