from django.forms import ModelForm

from .models import Repair, Console, ChoicesTypeOfConsole
from django import forms


class ConsoleForm(ModelForm):
    class Meta:
        model = Console
        fields = '__all__'
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'})
        }


class RepairForm(ModelForm):
    console_type = forms.ChoiceField(label='Тип приставки абонента', choices=ChoicesTypeOfConsole.choices)
    serial_number = forms.CharField(label='Серийный номер №', max_length=50)
    change_console_type = forms.ChoiceField(label='Тип подменной приставки', choices=ChoicesTypeOfConsole.choices)
    serial_number_change = forms.CharField(label='Серийный номер №', max_length=50)

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
            'console_type',
            'serial_number',
            'change_console_type',
            'serial_number_change',
            'description',

        )

    def save(self, commit=True):
        console_type = self.cleaned_data.pop('console_type')
        serial_number = self.cleaned_data.pop('serial_number')
        change_console_type = self.cleaned_data.pop('change_console_type')
        serial_number_change = self.cleaned_data.pop('serial_number_change')

        repair = super().save(commit=False)
        console, _ = Console.objects.get_or_create(type=console_type, serial_number=serial_number)
        change_console, _ = Console.objects.get_or_create(type=change_console_type, serial_number=serial_number_change)
        repair.console = console
        repair.change_console = change_console

        if commit:
            repair.save()

        return repair
