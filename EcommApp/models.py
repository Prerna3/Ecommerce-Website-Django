from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
# Create your models here.
class CustomeManager(models.Manager):
  def get_price_range(self,r1,r2):
    return self.filter(price__range=(r1,r2))
  
  def watchlist(self):
    return self.filter(category__exact="Watch")
  
  def laptoplist(self):
    return self.filter(category__exact="Laptop")
  
  def mobilelist(self):
     return self.filter(category__exact="Mobile")



class Product(models.Model):
  product_id = models.IntegerField(primary_key = True)
  product_name = models.CharField(max_length = 50)
  type = (("Watch","Watch"),("Mobile","Mobile"),("Laptop","Laptop"))
  category = models.CharField(max_length = 100, choices = type)
  desc = models.CharField(max_length = 255)
  price = models.IntegerField()
  image = models.ImageField(upload_to='pics')

  prod = CustomeManager() # customer manager
  objects = models.Manager() #default manager

  def proImage(self):
    return mark_safe(f"<img src='{self.image.url}' width='300px'>")
  
  def __str__(self):
    return(f"{self.product_name}")
  
class CartItem(models.Model):
  product = models.ForeignKey(Product,on_delete = models.CASCADE)
  quantity = models.PositiveIntegerField(default = 0)
  date_added = models.DateTimeField(auto_now_add = True)
  user = models.ForeignKey(User,on_delete = models.CASCADE,default = 1)

class Order(models.Model):
  order_id = models.CharField(max_length = 50)
  product = models.ForeignKey(Product,on_delete = models.CASCADE)
  quantity = models.PositiveIntegerField(default = 0)
  user = models.ForeignKey(User,on_delete = models.CASCADE,default = 1)
  date_added = models.DateTimeField(auto_now_add = True)
  is_completed = models.BooleanField(default = 'False')