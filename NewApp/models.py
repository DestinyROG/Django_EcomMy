from django.db import models

import os
import datetime
# Create your models here.

def get_file_path(request,filename):
    original_filename=filename
    nowTime= datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    urlname=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    def __str__(self):
        return self.name
    
all_category=[]
category=Category.objects.all()
for i in category:
    a=(i.urlname,i.urlname)
    if a in all_category:
        pass
    else:
        all_category.append(a)
    
class Product(models.Model):
    category=models.CharField(choices=all_category,max_length=255,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    small_description=models.CharField(max_length=255,null=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    category=models.CharField(max_length=255,null=True,blank=True)
    name=models.CharField(max_length=255,null=False,blank=False)
    product_image=models.ImageField(null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False,default=1)
    price=models.FloatField(null=False,blank=False)
    user=models.CharField(max_length=150,null=False,blank=False)
    def __str__(self):
        return self.name
    
def banner_image_file(request,filename):
    original_filename=filename
    nowTime= datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/Banner_image',filename)

_status=[('active','Active'),("","Non-Active")]

class Banner_image(models.Model):
    banner_image=models.ImageField(upload_to=banner_image_file,null=False,blank=False)
    category=models.CharField(choices=all_category,max_length=150,null=False,blank=False)
    status=models.CharField(choices=_status,null=False,blank=True,max_length=150)
    def __str__(self):
        return self.category