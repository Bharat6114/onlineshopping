from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Create your models here.
# DJANGO-ORM (Object relational mapping)


class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Products(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_detail = models.TextField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, null=True)
    category = models.ManyToManyField(Category, related_name="products_categoreis")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image1 = models.ImageField(upload_to="onlineshopping", null=True)
    cover_image2 = models.ImageField(upload_to="onlineshopping", null=True)
    cover_image3 = models.ImageField(upload_to="onlineshopping", null=True)

    def get_absolute_url(self):
        return reverse("single_news", kwargs={"pk": self.pk, "slug": self.slug})