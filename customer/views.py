from urllib import request
from django.shortcuts import render , redirect
from common.models import Customer
from seller.models import Product , Seller

# Create your views here.
def home(request) :
    products = Product.objects.all()
    return render(request,'customer/home.html',{'products':products})




def change_password(request) :

    msgs = ''

    if request.method == 'POST':

        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if new_password== confirm_password :
             if len(new_password) >= 8 :
                  customer = Customer.objects.get(id=request.session['customer'])
                  if customer.password == old_password :
                       Customer.objects.filter(id=request.session['customer']).update(password=confirm_password)
                       customer.password = confirm_password
                       customer.save()
                       msgs='successfull'
                  else :
                       msgs='invalid password'
             else :
                  msgs='should contain 8 letters'
        else:
             msgs = 'password does not match'

    return render(request,'customer/change_password.html',{'massage':msgs})


def master(request) :
    return render(request,'customer/master.html')

def my_cart(request) :
    return render(request,'customer/my_cart.html')

def my_order(request) :
    return render(request,'customer/my_order.html')

def product_details(request) :
    return render(request,'customer/product_details.html')

def profile(request) :
    profile = Customer.objects.get(id=request.session['customer'])
    return render(request,'customer/profile.html',{"customer":profile})

def logout(request) :
    del request.session['customer']
    request.session.flush()
    return redirect('common:home')