from django.db import models
from ecom.settings import AUTH_USER_MODEL
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category,related_name="category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-date_added"]
        
    def __str__(self):
        return self.title
    
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.product.title}({self.quantity})"
    
class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    
    def __str__(self):
        return self.user.username
    
    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.date = timezone.now()
            order.save()
        self.orders.clear()
        super().delete(*args, **kwargs)