# Generated by Django 4.1.5 on 2023-05-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=30),
        ),
    ]
