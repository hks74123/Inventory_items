from django.db import models

# Create your models here.

class Product(models.Model):
    Product_id=models.AutoField
    Product_image=models.FileField(upload_to='imgs',default='default.jpg', null=True,blank=True)
    Product_name=models.CharField(max_length=100)
    Product_price=models.IntegerField(max_length=10)
    Product_qty=models.IntegerField(max_length=12)
    Product_desc=models.CharField(max_length=250)
    Product_brand=models.CharField(max_length=80)   
    Product_color=models.CharField(max_length=70)
    Product_size=models.CharField(max_length=20)
    Product_category=models.CharField(max_length=80)
    Product_store=models.CharField(max_length=50)