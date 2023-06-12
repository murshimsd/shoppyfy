from django.urls import path
from . import views


urlpatterns = [

path('register',views.register_student,name='register'),
path('list',views.view_student,name='list'),
path('single_data/<int:id>',views.single_data_view,name='single_data'),
path('delete_data/<int:id>',views.delete,name='delete_data'),




]