from .models import Cart, CartItem


def cart_item_created(data: dict):
    CartItem.objects.create(
        id=data['id'],
        product_id=data['product'],
        quantity=data['quantity'],
    )


def cart_item_updated(data: dict):
    cart_item = CartItem.objects.get(id=data['id'])

    cart_item.product_id = data['product']
    cart_item.quantity = data['quantity']
    cart_item.save()


def cart_item_deleted(pk: int):
    CartItem.objects.filter(pk=pk).delete()


def cart_created(data: dict):
    Cart.objects.create(
        id=data['id'],
        user_id=data['user'],
        items=data['items'],
    )


def cart_updated(data: dict):
    cart = Cart.objects.get(id=data['id'])

    cart.user_id = data['user_id']
    cart.items = data['items']
    cart.save()


def cart_deleted(pk: int):
    Cart.objects.filter(pk=pk).delete()