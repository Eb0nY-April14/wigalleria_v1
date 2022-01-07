from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_cart(request):
    """
    A view that renders the cart contents page
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Adds the quantity of the specified product to the shopping cart
    """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', 'products')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'{product.name} has been added to your cart successfully!')

    request.session['cart'] = cart
    # print(request.session['cart'])
    return redirect(redirect_url)


# adjust_bag is the name of this function in Boutique Ado
def update_cart(request, item_id):
    """
    Updates the quantity of the specified product to the specified amount
    """

    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    # print(request.session['cart'])
    return redirect(reverse('view_cart'))


# remove_from_bag is the name of this function in Boutique Ado
def remove_from_cart(request, item_id):
    """Remove the item from the shopping bag"""

    # quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    # if quantity > 0:
    del_item = (cart.pop(item_id))
    print("Quantity of the deleted Product is: ", del_item)

    request.session['cart'] = cart
    return HttpResponse(status=200)
