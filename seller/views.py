
from urllib import request
from django.shortcuts import render , redirect
from common.models import Seller

from seller.models import Product

# Create your views here.
def home(request) :

    return render(request,'seller/home.html')

def change_password(request) :

    msgs = ''

    if request.method == 'POST':

        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if new_password== confirm_password :
             if len(new_password) >= 8 :
                  seller = Seller.objects.get(id=request.session['seller'])
                  if seller.password == old_password :
                       seller.password = confirm_password
                       seller.save()
                       msgs='successfull'
                  else :
                       msgs='invalid password'
             else :
                  msgs='should contain 8 letters'
        else:
             msgs = 'password does not match'

       

    return render(request,'seller/change_password.html',{'massage':msgs})



def add_product(request) :
        msg = ''
        if request.method == 'POST' :
            p_name = request.POST['name']
            p_description = request.POST['description']
            p_stock = request.POST['stock']
            p_code = request.POST['code']
            p_price = request.POST['price']
            p_image = request.FILES['image']

            product_exist = Product.objects.filter(seller = request.session['seller'],code = p_code).exists()

            if not product_exist :
                products = Product(
                    name = p_name,
                    description = p_description,
                    stock = p_stock,
                    price = p_price,
                    code = p_code,
                    photo = p_image,
                    seller_id = request.session['seller']
                )
                products.save()
                msg = 'added successfully'

            else:
                msg = 'product exist'


        
    

        return render(request,'seller/add_product.html',{"massage":msg})



def master(request) :
    seller = Seller.objects.get(id=request.session['seller'])
    return render(request,'seller/master.html',{'seller':seller})



def order_history(request) :
    return render(request,'seller/order_history.html')



def product_catalogue(request) :
    products = Product.objects.filter(seller=request.session['seller'])
    return render(request,'seller/product_catalogue.html',{'products':products})


def recent_order(request) :
    return render(request,'seller/recent_order.html')


def update_stock(request) :
    return render(request,'seller/update_stock.html')


def profile(request) :
    seller = Seller.objects.get(id=request.session['seller'])
    return render(request,'seller/profile.html',{"seller":seller})


def logout(request) :
    del request.session['seller']
    request.session.flush()
    return redirect('common:home')

