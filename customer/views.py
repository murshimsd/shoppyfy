
from urllib import request
from django.shortcuts import render , redirect
from common.models import Customer
from seller.models import Product , Seller
from . models import Cart

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
    cart_items = Cart.objects.filter(customer=request.session['customer'])
    return render(request,'customer/my_cart.html',{"cart_items":cart_items})

def my_order(request) :
    return render(request,'customer/my_order.html')

def product_details(request,pid) :
    products = Product.objects.get(id = pid)
    msg = ''
    if request.method == 'POST':
        stocks = request.POST['stock']
        cart_exist = Cart.objects.filter(product = pid,customer = request.session['customer']).exists()
        if not cart_exist :

            cart = Cart(customer_id=request.session['customer'],product_id=pid,stock=stocks)
            cart.save()
            return redirect('customer:my_cart')
        else :
            msg = 'already in cart'

    
    return render(request,'customer/product_details.html',{"product":products,"msg":msg})

def profile(request) :
    profile = Customer.objects.get(id=request.session['customer'])
    return render(request,'customer/profile.html',{"customer":profile})

def logout(request) :
    del request.session['customer']
    request.session.flush()
    return redirect('common:home')

def edit_profile(request) :
    customer = Customer.objects.get(id=request.session['customer'])

    msg = ''
    if request.method == 'POST':
        # new_photo = request.FILES['photo']
        new_name = request.POST['name']
        new_address = request.POST['address']
        new_email = request.POST['email']

        customer.name = new_name
        customer.email = new_email
        customer.address = new_address
        # if new_photo == '':
        #     customer.photo = customer.photo
        # else: 
        #     customer.photo= new_photo
        customer.save()
        msg = 'successfully updated'
    return render(request,'customer/update_form.html',{'customer':customer,'msgs':msg})

