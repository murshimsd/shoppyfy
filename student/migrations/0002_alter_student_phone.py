# Generated by Django 4.1.5 on 2023-05-29 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
