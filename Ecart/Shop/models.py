from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default='')
    sub_category = models.CharField(max_length=50, default='')
    price = models.IntegerField()
    publish_date= models.DateField()
    images = models.ImageField(upload_to='Shop/images',default='')

    def __str__(self):
        return  self.product_name

