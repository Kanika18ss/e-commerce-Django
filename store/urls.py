from django.urls import path
from . import views
from store.controller import authview, cart , wishlist ,checkout , order

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name="collections"),
    path("collections/<str:slug>", views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),
    
    
    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),
    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    path('wishlist', wishlist.index, name="wishlist"),
    path('add-to-wishlist', wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', wishlist.deletewishlistitem, name="deletewishlistitem"),
    path('checkout', checkout.checkout, name="checkout"),
    
    path('placeorder/', checkout.place_order, name='placeorder'),
    path('add_address/', checkout.add_address, name='add_address'),
    path('edit_address/<int:address_id>/', checkout.edit_address, name='edit_address'),
    path('proceed-to-pay', checkout.razorpaycheck),
    path('my-orders', order.index, name="myorders"),
    path('view-order/<str:t_id>', order.vieworder, name="orderview"),
    path('return-order/<str:t_id>', order.returnorder, name="return_order"),
    
    path('request-return/<int:item_id>/', order.request_return, name='request_return'),
    
    path('get-address-data/', checkout.get_address_data, name='get_address_data'),
]

