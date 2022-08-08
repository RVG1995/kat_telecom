from django.contrib import admin
from .models import Repair, Console
from .forms import RepairForm

from rangefilter.filters import DateRangeFilter


class ConsoleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'serial_number',
        'pub_date')
    list_filter = (('pub_date', DateRangeFilter),)
    empty_value_display = "-пусто-"


class RepairAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'statement',
        'number_of_contract',
        'name',
        'fixing',
        'ports_wan',
        'stickers',
        'body',
        'console',
        'change_console',
        'description',
        'pub_date',
    )
    list_filter = (('pub_date', DateRangeFilter),)
    empty_value_display = "-пусто-"
    search_fields = ['name', 'number_of_contract']
    form = RepairForm


admin.site.register(Repair, RepairAdmin)
admin.site.register(Console, ConsoleAdmin)
