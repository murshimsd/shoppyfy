# Generated by Django 4.1.5 on 2023-05-11 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_seller_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='seller',
            name='user_name',
            field=models.IntegerField(default=1),
        ),
    ]
