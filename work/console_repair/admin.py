from django.contrib import admin
from .models import Repair


class RepairAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
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


admin.site.register(Repair, RepairAdmin)
