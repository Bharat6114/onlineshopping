from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
          verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_price = models.IntegerField(max_length=5)
    count = models.IntegerField(default=0)

    category = models.ManyToManyField(Category, related_name="product_categoreis")
    product_image = models.ImageField(upload_to="online_shopping", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
