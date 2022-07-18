from django.db import models


class OrderOutfit(models.Model):
    order_outfit = models.CharField('Заказ-наряд', max_length=50)
    customer = models.CharField('Заказчик', max_length=50)
    telephone_number = models.CharField('Телефон', max_length=50)
    town = models.CharField('Поселок', max_length=50)
    street = models.CharField('Улица', max_length=50)
    house = models.CharField('Дом', max_length=50)
    number_of_contract = models.IntegerField("Номер договора")
    pub_date = models.DateField(auto_now_add=True)
    sum = models.IntegerField("Сумма", blank=True, null=True)

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Заказ-наряд"
        verbose_name_plural = "Заказ-наряд"
