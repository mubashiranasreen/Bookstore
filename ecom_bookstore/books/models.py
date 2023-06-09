from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20, default="#000000", unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True, blank=True)
    image_urls = models.CharField(max_length=2083, blank=True)
    follow_author = models.CharField(max_length=2083, blank=True)
    book_available = models.BooleanField()

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title


class MyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, null=True, blank=True)
    pfp = models.ImageField(upload_to='profiles', null=True, blank=True, height_field=None, width_field=None,
                            max_length=None)
    bio = models.CharField(max_length=200, null=True, blank=True)
    favorites = models.ManyToManyField(Book, related_name='favorites', blank=True)
    delivery_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.total_price


class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.book}'

    @property
    def total_price(self):
        return self.book.price * self.quantity
