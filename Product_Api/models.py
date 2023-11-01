from django.db import models


class Category(models.Model):
    product_category = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_category
    
class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.variant_name

class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.color_name

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.size_name

class Product(models.Model):
    name=models.CharField(max_length=100)
    description =models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True) 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    created_at=models.DateTimeField(auto_now_add=True)
    quantity_type = models.ForeignKey(QuantityVariant , blank=True, null=True , on_delete=models.PROTECT)
    color_type = models.ForeignKey(ColorVariant , blank=True, null=True , on_delete=models.PROTECT)
    size_type = models.ForeignKey(SizeVariant , blank=True, null=True , on_delete=models.PROTECT)

def __str__(self):
        return self.name

class ProductImages(models.Model):
    product = models.ForeignKey(Product , on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products/')

def __str__(self):
    return f"Image for {self.product.name}"