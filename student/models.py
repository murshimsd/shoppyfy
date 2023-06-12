from django.db import models

# Create your models here.

class Student (models.Model) :
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='student/')
    phone = models.BigIntegerField()


    class Meta :
        db_table = 'student_tb'


