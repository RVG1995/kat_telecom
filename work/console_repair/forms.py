from django.forms import ModelForm

from .models import Repair


class RepairForm(ModelForm):
    class Meta:
        model = Repair
        fields = ('statement', 'number_of_contract',
                  'name', 'fixing', 'ports_wan',
                  'stickers', 'body', 'console',
                  'serial_number_console', 'change_console',
                  'serial_number_change_console', 'description')

# CHOICES_FIXING = (
#     (1, 'Да'),
#     (2, 'Нет'),
# )
# CHOICES_PORTS_WAN = (
#     (1, 'Исправны'),
#     (2, 'Не исправны'),
#     (3, 'Невозможно проверить'),
#
# )
# CHOICES_STICKERS = (
#     (1, 'Без повреждений'),
#     (2, 'Отсутсвуют'),
# )
# CHOICES_BODY = (
#     (1, 'Без повреждений'),
#     (2, 'Потертости'),
#     (3, 'Поврежден'),
# )
# CHOICES_TYPE_OF_CONSOLE = (
#     (1, 'NTE-RG-1402F'),
#     (2, 'NTE-RG-1402G'),
#     (3, 'NTE-RG-1400F'),
#     (4, 'NTE-RG-1400G'),
#     (5, 'NTE-RG-1400'),
#     (6, 'NTE-2')
# )
#
#
# class Repair(forms.Form):
#     statement = forms.IntegerField(label="Дефектная ведомость", max_length=10)
#     number_of_contract = forms.IntegerField(label="Номер договора", max_length=10)
#     first_name = forms.CharField(label='Имя', max_length=50)
#     second_name = forms.CharField(label='Фамилия', max_length=50)
#     patronymic = forms.CharField(label='Отчество', max_length=50)
#     date = forms.DateField(label='ДАТА ВЕДОМОСТИ', input_format='%d/%m/%Y')
#     fixing = forms.ChoiceField(
#         label='Крепежные элементы в порядке',
#         choices=CHOICES_FIXING)
#     ports_wan = forms.ChoiceField(label='Работоспособность портов',
#                                   choices=CHOICES_PORTS_WAN)
#     stickers = forms.ChoiceField(label='Заводские наклейки/пломбы',
#                                  choices=CHOICES_STICKERS)
#     body = forms.ChoiceField(label='Целостность корпуса',
#                              choices=CHOICES_BODY)
#     console = forms.ChoiceField(label='Тип приставки абонента',
#                                 choices=CHOICES_TYPE_OF_CONSOLE)
#     serial_number_console = forms.CharField(label='Серийный номер №',
#                                             max_length=50)
#     change_console = forms.ChoiceField(label='Тип подменной приставки',
#                                        choices=CHOICES_TYPE_OF_CONSOLE)
#     serial_number_change_console = forms.CharField(label='Серийный номер №',
#                                                    max_length=50)
#     description = forms.TextField('Заключение о состоянии оборудования',
#                                   max_length=200)
#     pub_date = forms.DateTimeField(label="Дата публикации",
#                                    auto_now_add=True
#                                    )
#
#
# class Meta:
#     ordering = ("-pub_date",)
