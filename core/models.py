from django.db import models


class CartItem(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FastStreamLogs(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    error = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
