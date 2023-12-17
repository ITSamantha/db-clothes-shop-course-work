from orders.models import Cart


def get_cart_products(user):
    cart = Cart.objects.filter(user=user)
    return cart
