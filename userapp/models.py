from django.contrib.auth.models import User
from django.db import models

from myapp.models import Book1


class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(Book1)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(Book1,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)