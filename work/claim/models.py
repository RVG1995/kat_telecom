from django.db import models


class ChoicesTypeOfStatus(models.TextChoices):
    IN_WORK_OFFICE = 'IWO', 'В работе(ОФИС)'
    IN_WORK_VALERA = 'IWV', 'В работе(ВАЛЕРА)'
    COMPLETED_OFFICE = 'CO', 'Выполнена(ОФИС)'
    COMPLETED_VALERA = 'CV', 'Выполнена(ВАЛЕРА)'
    CANSEL = 'C', 'ОТМЕНА'


class ChoicesTypeOfReason(models.TextChoices):
    OPTIC_FAIL = 'OF', 'OF'
    NOT_ENOUGH_SIGNAL = 'NES', 'Не хватает сигнала'
    OTHER = 'O', 'Другое'


class Claim(models.Model):
    order_outfit = models.CharField('ЗАКАЗ-НАРЯД', max_length=50, blank=True, )
    customer = models.CharField('ЗАКАЗЧИК', max_length=50)
    date_of_the_application = models.DateField('ДАТА ОБРАЩЕНИЯ', auto_now_add=True)
    number_of_contract = models.CharField("НОМЕР ДОГОВОРА", max_length=10)
    reason = models.CharField('ПРИЧИНА', choices=ChoicesTypeOfReason.choices, max_length=50)
    telephone_number = models.CharField('ТЕЛЕФОН', max_length=50)
    town = models.CharField('ПОСЕЛОК', max_length=50)
    street = models.CharField('УЛИЦА', max_length=50)
    house = models.CharField('ДОМ', max_length=50)
    comment_from_subscriber = models.TextField('КОММЕНТАРИЙ ОТ АБОНЕНТА', max_length=150, blank=True)
    status = models.CharField('СТАТУС', choices=ChoicesTypeOfStatus.choices, max_length=4, blank=True, null=True)
    repair_date = models.DateField('ДАТА РЕМОНТА', blank=True, null=True)
    comment_from_worker = models.TextField('КОММЕНТАРИЙ ОТ МОНТАЖНИКОВ', max_length=150, blank=True)
    sum = models.IntegerField("СУММА", blank=True, null=True)

    class Meta:
        ordering = ("-date_of_the_application",)
        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"

        constraints = (
            models.CheckConstraint(
                name='valid_status_state_choice',
                check=models.Q(status__in=ChoicesTypeOfStatus.values)
            ),
            models.CheckConstraint(
                name='valid_reason_state_choices',
                check=models.Q(reason__in=ChoicesTypeOfReason.values)
            )
        )

    def get_status(self):
        return ChoicesTypeOfStatus(self.status)

    def get_reason(self):
        return ChoicesTypeOfReason(self.reason)
