# Generated by Django 3.1.6 on 2021-04-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.CharField(default='00000', max_length=5),
        ),
    ]
