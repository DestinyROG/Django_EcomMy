# Generated by Django 4.1.5 on 2023-02-19 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0007_alter_banner_image_category_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner_image',
            name='category',
            field=models.CharField(choices=[('shoes', 'shoes'), ('fashions', 'fashions'), ('mobiles', 'mobiles'), ('laptop', 'laptop')], max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('shoes', 'shoes'), ('fashions', 'fashions'), ('mobiles', 'mobiles'), ('laptop', 'laptop')], max_length=255),
        ),
    ]