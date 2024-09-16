from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There´s nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    OrderForm = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_from': order_form,
    }

    return render(request, template, context)