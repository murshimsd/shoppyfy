from django.db import models
from common.models import Customer
from seller.models import Product

# Create your models here.

class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    stock = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart_tb'


class Orders(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'order_tb'