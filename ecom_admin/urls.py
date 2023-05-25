from django.urls import path
from . import views


app_name = "ecom_admin"

urlpatterns = [
    path('home',views.home,name='home'),
    path('approve_seller',views.approve_seller,name='approve_seller'),
    path('view_seller',views.view_seller,name='view_seller'),
    path('view_customer',views.view_customer,name='view_customer'),
    path('master',views.master,name='master'),
    path('logout',views.logout,name='logout'),
    path('password',views.password,name='password'),
    path('approve/<int:sid>',views.approvesell,name='approve'),
    path('remove_seller/<int:s_id>',views.remove_seller,name='remove_seller'),
    path('remove_cus/<int:cid>',views.remove_customer,name='remove_cus')
   
]