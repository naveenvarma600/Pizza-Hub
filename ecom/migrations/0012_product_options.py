# Generated by Django 3.1.6 on 2021-05-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0011_auto_20210510_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='options',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]