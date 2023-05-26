
from django.conf import settings
from django.shortcuts import render , redirect
from ecom_admin.models import Admin
from common.models import Seller,Customer
from django.core.mail import send_mail
from ecommerce.settings import EMAIL_HOST_USER

# Create your views here.

def home(request) :
    return render(request,'ecom_admin/home.html')

def approve_seller(request) :
    seller = Seller.objects.filter(status ="pending")
    return render(request,'ecom_admin/approve_seller.html',{"sellers":seller})

def approvesell(request,sid):
 
    seller=Seller.objects.get(id=sid)
    msg='your seller request is approved . your usr id is'+str(seller.user_name)+'password is'+str(seller.password)
    seller.status='approved'
    seller.save()
    send_mail(
        'subject',
        msg,
        settings.EMAIL_HOST_USER,
        [seller.e_mail]
    )
  
    return redirect("ecom_admin:view_seller")

def remove_seller(request,s_id):
    seller = Seller.objects.get(id=s_id)
    seller.delete()
    return render(request,"ecom_admin/approve_seller.html",{"seller":seller})
    

def password(request):
    msg = ''
    if request.method == 'POST':
        old_passwords = request.POST['old_password']
        new_passwords = request.POST['new_password']
        con_passwords= request.POST['confirm_password']

        if new_passwords == con_passwords :
            admin = Admin.objects.get(id=request.session['admins'])
            if len(new_passwords) >= 8 :
                if old_passwords == admin.password :
                    admin.password = con_passwords
                    msg = 'successfull'
                    admin.save()
                else :
                    msg = 'old password is wrong'
            else :
                msg = 'not 8 letters'
        else :
            msg = 'wrong password'


    return render(request,'ecom_admin/password.html',{"msg":msg})

def view_customer(request) :
    customer = Customer.objects.all()
    return render(request,'ecom_admin/view_customer.html',{"customers":customer})

def view_seller(request) :
    seller = Seller.objects.filter(status = 'approved')

    return render(request,'ecom_admin/view_seller.html',{"sellers":seller})

def master(request) :
    return render(request,'ecom_admin/master.html')

def logout(request) :
    del request.session['admins']
    request.session.flush()
    return redirect('common:home')

def remove_customer(request,cid) :
    customer = Customer.objects.get(id=cid)
    customer.delete()
    return redirect("ecom_admin:view_customer")


    