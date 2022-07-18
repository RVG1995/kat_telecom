from django.forms import ModelForm

from .models import Repair


class RepairForm(ModelForm):
    class Meta:
        model = Repair
        fields = (
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
            'description')
