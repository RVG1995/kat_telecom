from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class RepairBodyState(models.TextChoices):
    DAMAGED = 'D', 'Поврежден'
    SCRATCHED = 'S', 'Потертости'
    INTACT = 'I', 'Без повреждений'


class ChoicesTypeOfConsole(models.TextChoices):
    NTE_RG_1402_F = '1', 'NTE-RG-1402F'
    NTE_RG_1402_G = '2', 'NTE-RG-1402G'
    NTE_RG_1400_F = '3', 'NTE-RG-1400F'
    NTE_RG_1400_G = '4', 'NTE-RG-1400G'
    NTE_RG_1400 = '5', 'NTE-RG-1400'
    NTE_2 = '6', 'NTE-2'


class Repair(models.Model):
    CHOICES_FIXING = (
        (True, 'Да'),
        (False, 'Нет'),
    )
    CHOICES_PORTS_WAN = (
        (True, 'Исправны'),
        (False, 'Не исправны'),
        (None, 'Невозможно проверить'),
    )
    CHOICES_STICKERS = (
        (True, 'Без повреждений'),
        (False, 'Отсутсвуют'),
    )

    statement = models.CharField("Дефектная ведомость", max_length=10)
    number_of_contract = models.CharField("Номер договора", max_length=10)
    name = models.CharField('ФИО', max_length=150)
    fixing = models.BooleanField(
        'Крепежные элементы в порядке',
        choices=CHOICES_FIXING,
    )
    ports_wan = models.BooleanField(
        'Работоспособность портов',
        choices=CHOICES_PORTS_WAN,
        null=True,
    )
    stickers = models.BooleanField(
        'Заводские наклейки/пломбы',
        choices=CHOICES_STICKERS,
    )
    body = models.CharField(
        'Целостность корпуса',
        choices=RepairBodyState.choices,
        max_length=1)
    console = models.CharField(
        'Тип приставки абонента',
        choices=ChoicesTypeOfConsole.choices,
        max_length=2)
    serial_number_console = models.CharField(
        'Серийный номер №',
        max_length=50)
    change_console = models.CharField(
        'Тип подменной приставки',
        choices=ChoicesTypeOfConsole.choices,
        max_length=2)
    serial_number_change_console = models.CharField(
        'Серийный номер №',
        max_length=50)
    description = models.TextField(
        'Заключение о состоянии оборудования',
        max_length=200)
    pub_date = models.DateField(
        "Дата публикации",
        auto_now_add=True
    )

    class Meta:
        ordering = ("-pub_date",)
        constraints = (
            models.CheckConstraint(
                name='valid_body_state_choice',
                check=models.Q(body__in=RepairBodyState.values)
            ),
            models.CheckConstraint(
                name='valid_console_choice',
                check=models.Q(console__in=ChoicesTypeOfConsole.values)
            ),
        )
        verbose_name = "Дефектные ведомости"
        verbose_name_plural = "Дефектные ведомости"

    def __str__(self):
        return self.name

    def get_body(self):
        return RepairBodyState(self.body)

    def get_console(self):
        return ChoicesTypeOfConsole(self.console)

    def get_change_console(self):
        return ChoicesTypeOfConsole(self.change_console)
