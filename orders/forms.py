from django import forms
from django.forms import inlineformset_factory

from .models import Order, Address

AddressFormSet = inlineformset_factory(Order, Address, fields=('address',))


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'type', 'delivery_date', 'file']
