# Generated by Django 3.2.9 on 2022-01-10 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_image', models.FileField(blank=True, default='default.jpg', null=True, upload_to='imgs')),
                ('Product_name', models.CharField(max_length=100)),
                ('Product_price', models.IntegerField(max_length=10)),
                ('Product_qty', models.IntegerField(max_length=12)),
                ('Product_desc', models.CharField(max_length=250)),
                ('Product_brand', models.CharField(max_length=80)),
                ('Product_color', models.CharField(max_length=70)),
                ('Product_size', models.CharField(max_length=20)),
                ('Product_category', models.CharField(max_length=80)),
                ('Product_store', models.CharField(choices=[('1', 'Store1'), ('2', 'Store2'), ('3', 'Store3'), ('4', 'Store4'), ('5', 'Store5')], max_length=50)),
            ],
        ),
    ]