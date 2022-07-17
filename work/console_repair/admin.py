from django.contrib import admin
from .models import Repair


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
        'serial_number_console',
        'change_console',
        'serial_number_change_console',
        'description',
        'pub_date',
    )
    list_filter = ('pub_date',)
    empty_value_display = "-пусто-"
    search_fields = ['name', 'number_of_contract']


admin.site.register(Repair, RepairAdmin)
