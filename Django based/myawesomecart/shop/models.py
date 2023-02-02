from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category= models.CharField(max_length=50,default="")
    subcategory= models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    publish_date=models.DateField()
    images=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=80,default="")
    phone= models.CharField(max_length=80,default="")
    msg= models.CharField(max_length=300,default="")

    def __str__(self):
        return self.name