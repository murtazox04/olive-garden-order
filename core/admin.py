from django.contrib import admin
from .models import Order, CartItem, Cart, KafkaError

admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(KafkaError)
