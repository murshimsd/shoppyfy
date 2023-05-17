from django.urls import path
from . import views


app_name = "ecom_admin"

urlpatterns = [
    path('home',views.home,name='home'),
    path('approve_seller',views.approve_seller,name='approve_seller'),
    path('view_seller',views.view_seller,name='view_seller'),
    path('view_customer',views.view_customer,name='view_customer'),
    path('master',views.master,name='master'),
   
]