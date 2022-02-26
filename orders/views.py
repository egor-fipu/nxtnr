from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import OrderForm, AddressFormSet
from .models import Order


class NewOrder(View):

    def get(self, request, *args, **kwargs):
        form = OrderForm()
        address_form = AddressFormSet()
        context = {'form': form, 'address_form': address_form}
        return render(request, 'orders/new_order.html', context)

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST, files=request.FILES or None)
        address_form = AddressFormSet(request.POST)
        if form.is_valid() and address_form.is_valid():
            order = form.save()
            address_form.instance = order
            address_form.save()
            return redirect('orders_list')
        context = {'form': form, 'address_form': address_form}
        return render(request, 'orders/new_order.html', context)


class OrdersList(ListView):
    template_name = 'orders/orders_list.html'
    context_object_name = 'orders'
    model = Order
