# Generated by Django 4.2.7 on 2023-12-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostacos', '0006_category_alter_dish_photo_dish_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
