# Generated by Django 4.1.5 on 2023-05-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_seller_password_seller_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='ac_holder_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='seller',
            name='ac_no',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='seller',
            name='branch',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='seller',
            name='ifsc',
            field=models.CharField(default='', max_length=20),
        ),
    ]