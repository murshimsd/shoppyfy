from django.urls import path
from . import views


app_name = "customer"

urlpatterns = [
    path('home',views.home,name='home'),
    path('change_password',views.change_password,name='change_password'),
    path('logout',views.logout,name='logout'),
    path('master',views.master,name='master'),
    path('my_cart',views.my_cart,name='my_cart'),
    path('my_order',views.my_order,name='my_order'),
    path('product_details',views.product_details,name='product_details'),
    path('profile',views.profile,name='profile')

    
]