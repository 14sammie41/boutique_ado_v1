from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    if not settings.STRIPE_PUBLIC_KEY or not settings.STRIPE_SECRET_KEY:
        messages.error(request, 'Stripe keys are not configured properly.')
        return redirect(reverse('view_bag'))
    
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    
    try:
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
    except stripe.error.StripeError as e:
        messages.error(request, f'Stripe error: {e}')
        return redirect(reverse('view_bag'))
    
    print(intent)
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }
    
    return render(request, template, context)
        