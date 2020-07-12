from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Fiction', 'Fiction'),
        ('Romantic', 'Romantic'),
        ('Thriller', 'Thriller'),
        ('Rom-Com', 'Rom-Com'),
        ('Classic', 'Classic'),
        ('LGBTQ', 'LGBTQ'),
        ('Non-Fiction', 'Non-Fiction'),
    )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=200, choices=CATEGORY)
    Price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Our for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, choices=STATUS)
    date_created = models.DateField(auto_now_add=True)
