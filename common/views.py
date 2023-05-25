import random
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.conf import settings

from common.models import Seller
from common.models import Customer
from ecom_admin.models import Admin
from django.http import JsonResponse


# Create your views here.

def home(request) :
    return render(request,'common/home.html')


def customer_login(request) :
    msg = ''
    if request.method == 'POST' :
        emails = request.POST['mail']
        passwords = request.POST['password']

        try:
            customer = Customer.objects.get(email=emails,password=passwords)
            request.session['customer'] = customer.id
            request.session['customer_name'] = customer.name
            request.session['customer_photo'] = customer.photo.url
            return redirect('customer:home')

        except :
            msg = 'incorrect'
    
    return render(request,'common/customer_login.html',{'msg':msg})


def customer_register(request) :
    msg = ''
    if request.method == 'POST' :
        cus_name = request.POST['name']
        cus_address = request.POST['address']
        cus_gender = request.POST['gender']
        cus_phone = request.POST['phone']
        cus_email = request.POST['email']
        cus_password = request.POST['password']
        cus_photo = request.FILES['photo']

        customer_exist = Customer.objects.filter(email=cus_email).exists()
        if not customer_exist :

            new_customer = Customer(
                name = cus_name,
                address = cus_address,
                gender = cus_gender,
                phone = cus_phone,
                email = cus_email,
                password = cus_password,
                photo = cus_photo
            )
            new_customer.save()
            msg = 'successfulled'

        else :
            msg = 'already existed mail'

    return render(request,'common/customer_register.html',{'massage':msg})



def seller_login(request) :

    msgs = ''

    if request.method == 'POST':

        user_names = request.POST['user_name']
        passwords = request.POST['password']

        try:
            seller = Seller.objects.get(user_name = user_names , password = passwords )
            request.session['seller'] = seller.id
            request.session['seller_name'] = seller.name
            request.session['seller_photo'] = seller.photo.url
            return redirect('seller:home')

        except :
            msgs = 'incorrect'




    return render(request,'common/seller_login.html',{"msg":msgs})




def seller_register(request) :
    msgs = ''
    if request.method == 'POST' :
        seller_name = request.POST['name']
        seller_address = request.POST['address']
        seller_email = request.POST['email']
        seller_gender = request.POST['gender']
        seller_phone = request.POST['phone']
        seller_photo = request.FILES['photo']
        seller_company = request.POST['company']
        seller_ac_holder_name = request.POST['ac_holder_name']
        seller_ifsc = request.POST['ifsc']
        seller_branch = request.POST['branch']
        seller_ac_no = request.POST['ac_no']
        s_username = random.randint(1111,9999)
        s_password = 'sel-'+str(s_username)

        seller_exist = Seller.objects.filter(e_mail = seller_email).exists()

        if not seller_exist :
            
            new_seller = Seller(
            name = seller_name,
            address = seller_address,
            e_mail = seller_email,
            gender = seller_gender,
            phone_no = seller_phone,
            photo = seller_photo,
            company_name = seller_company,
            ac_holder_name = seller_ac_holder_name,
            ifsc = seller_ifsc,
            branch = seller_branch,
            ac_no = seller_ac_no,
            user_name = s_username,
            password = s_password
            )
            new_seller.save()
            msgs = 'created successfully'

        else :

            msgs = 'email already exist'

            



      
        msg = "hi user name is :"+str(s_username)+'and your passwor :'+s_password
        # send_mail(
        #     'user name and password',
        #     msg,
        #     settings.MAIL_HOST_USER,
        #     [seller_email]
        # )

    return render(request,'common/seller_register.html',{"massage":msgs})




def master(request) :
    return render(request,'common/master.html')




def admin_login(request) :
    msg = ''
    if request.method == 'POST':
        u_name = request.POST['user_name']
        passwords = request.POST['password']

        try:
            admins = Admin.objects.get(user_id = u_name,password=passwords)
            request.session['admins'] = admins.id
            msg = 'correct'
            return redirect('ecom_admin:home')
        except:
            msg = 'incorrect'

    return render(request,'common/admin_login.html',{"msg":msg})

def check_mail(request):
    email_ajax = request.POST['customerEmail'] #recieved from ajax
    exist = Customer.objects.filter(email=email_ajax).exists()
    return JsonResponse({"email_exist":exist})

def check_mail_seller(request):
    email_ajax = request.POST['seller_mail'] #recieved from ajax
    exist = Seller.objects.filter(e_mail=email_ajax).exists()
    return JsonResponse({"email_exist":exist})




