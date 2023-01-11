from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)


class Brand(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    catergory = models.ForeignKey(Category, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()


class Address(models.Model):
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=4)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)


class Cart(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'PENDING'),
        (PAYMENT_STATUS_COMPLETE, 'COMPLETE'),
        (PAYMENT_STATUS_FAILED, 'FAILED')
    ]
    ordered_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
