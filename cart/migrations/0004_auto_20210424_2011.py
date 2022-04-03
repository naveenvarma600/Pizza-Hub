# Generated by Django 3.1.6 on 2021-04-24 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_auto_20210421_2150'),
        ('cart', '0003_auto_20210424_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_entry', to='cart.cart'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_entry', to='ecom.product'),
        ),
    ]
