from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Campaign)
admin.site.register(Payment)
admin.site.register(Shipping)
admin.site.register(Seller)