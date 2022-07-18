from django.forms import ModelForm

from .models import OrderOutfit


class OrderOutfitForm(ModelForm):
    class Meta:
        model = OrderOutfit
        fields = (
            'order_outfit',
            'customer',
            'telephone_number',
            'town',
            'street',
            'house',
            'number_of_contract',
            'sum',)
