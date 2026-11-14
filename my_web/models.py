from django.db import models
from datetime import datetime



class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    
    
    
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='image/')
    stock = models.IntegerField()
    def __str__(self):
        return self.product_name
    

class Order(models.Model):
    product_id = models.ManyToManyField(Product)
    customer_name = models.CharField(max_length=200)
    count = models.IntegerField()
    status_payment = models.BooleanField(default=False)
    def __str__(self):
        return self.customer_name
    
    