from django.shortcuts import redirect

def auth_seller(func):
    def wrapper(request, *args, **kwargs):
        if 'seller' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('common:home')
           
    return wrapper