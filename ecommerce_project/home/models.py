from msilib.schema import Class
from tabnanny import verbose
from django.db import models
from django.urls import reverse

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50,unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    def __str__(self) -> str:
        return self.name


class products(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    categ=models.ForeignKey(category,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'products'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('product_detail',args=[self.categ.slug , self.slug])

    def __str__(self) -> str:
        return self.name