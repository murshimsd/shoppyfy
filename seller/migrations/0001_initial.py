# Generated by Django 4.1.5 on 2023-05-15 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0007_alter_customer_table_alter_seller_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('stock', models.BigIntegerField()),
                ('product_code', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='seller/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
        ),
    ]
