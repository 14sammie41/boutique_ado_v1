from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51SHl0bPW2LJfqxTFvgOCrDwzi0lCO0gMTIiumVFLMjmK6XCE978kF1KLV2OoElLa4g7bQd9anLjG9CXpcV3yd9s800k0x4lmHJ',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)
        