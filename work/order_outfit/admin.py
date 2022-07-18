from django.contrib import admin
from .models import OrderOutfit


class OrderOutfitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_outfit',
        'customer',
        'telephone_number',
        'number_of_contract',
        'sum',
        'pub_date',
    )
    list_filter = ('pub_date',)
    search_fields = ['order_outfit', 'customer', 'telephone_number', 'number_of_contract']


admin.site.register(OrderOutfit, OrderOutfitAdmin)

