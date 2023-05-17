from django.db import models
from common.models import Seller

# Create your models here.

class Product(models.Model) :
    name = models.CharField(max_length= 30 )
    description = models.CharField(max_length= 100 )
    stock = models.BigIntegerField()
    code = models.CharField(max_length= 30 )
    price = models.FloatField()
    photo = models.ImageField(upload_to  = 'seller/' )
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)


    class Meta:
        db_table = 'product_tb'



