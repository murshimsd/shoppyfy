from django.shortcuts import render

# Create your views here.

def home(request) :
    return render(request,'ecom_admin/home.html')

def approve_seller(request) :
    return render(request,'ecom_admin/approve_seller.html')

def view_customer(request) :
    return render(request,'ecom_admin/view_customer.html')

def view_seller(request) :
    return render(request,'ecom_admin/view_seller.html')

def master(request) :
    return render(request,'ecom_admin/master.html')