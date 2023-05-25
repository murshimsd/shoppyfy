from django.urls import path
from . import views


app_name = "seller"

urlpatterns = [
    path('add_product',views.add_product,name='add_product'),
    path('change_password',views.change_password,name='change_password'),
    path('home',views.home,name='home'),
    path('master',views.master,name='master'),
    path('order_history',views.order_history,name='order_history'),
    path('product_catalogue',views.product_catalogue,name='product_catalogue'),
    path('recent_order',views.recent_order,name='recent_order'),
    path('update_stock',views.update_stock,name='update_stock'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name='logout'),
    path('change_profile',views.change_profile,name='change_profile'),
    path('new_profile',views.new_profile,name='new_profile')

    
]