from django.db import models

# Create your models here.


class Category(models.Model):
    MEN = 'MEN'
    WOMEN = 'WOMEN'
    KIDS = 'KIDS'
    CATALOG_CHOICES = [
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (KIDS, 'Kids'),
    ]
    type = models.CharField(max_length=200)
    catalog = models.CharField(max_length=200, choices=CATALOG_CHOICES)


class Product(models.Model):
    title = models.CharField(max_length=200)
    articule = models.CharField(max_length=30, unique=True)
    price = models.FloatField()
    currency = models.CharField(max_length=20)
    count = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


