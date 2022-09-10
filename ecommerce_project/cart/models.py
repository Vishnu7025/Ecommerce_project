from operator import mod
from django.db import models
from home.models import products
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank=True)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self) :
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product

class Review(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    product = models.ForeignKey(products,models.CASCADE)
    comment = models.TextField(max_length=250,blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
