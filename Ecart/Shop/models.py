from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=300)
    publish_date= models.DateField()


