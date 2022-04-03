# Generated by Django 3.1.6 on 2021-04-21 16:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecom', '0005_auto_20210421_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='buyers',
            field=models.ManyToManyField(blank=True, related_name='product_buy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='product_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
