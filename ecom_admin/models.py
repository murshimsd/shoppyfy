from django.db import models

# Create your models here.
class Admin (models.Model) :
    user_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


    class Meta :
        db_table = 'admin_tb'