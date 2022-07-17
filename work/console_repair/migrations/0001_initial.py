# Generated by Django 4.0.6 on 2022-07-17 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.IntegerField(verbose_name='Дефектная ведомость')),
                ('number_of_contract', models.IntegerField(verbose_name='Номер договора')),
                ('name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('fixing', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], verbose_name='Крепежные элементы в порядке')),
                ('ports_wan', models.BooleanField(choices=[(True, 'Исправны'), (False, 'Не исправны'), (None, 'Невозможно проверить')], null=True, verbose_name='Работоспособность портов')),
                ('stickers', models.BooleanField(choices=[(True, 'Без повреждений'), (False, 'Отсутсвуют')], verbose_name='Заводские наклейки/пломбы')),
                ('body', models.CharField(choices=[('D', 'Поврежден'), ('S', 'Потертости'), ('I', 'Без повреждений')], max_length=1, verbose_name='Целостность корпуса')),
                ('console', models.CharField(choices=[('1', 'NTE-RG-1402F'), ('2', 'NTE-RG-1402G'), ('3', 'NTE-RG-1400F'), ('4', 'NTE-RG-1400G'), ('5', 'NTE-RG-1400'), ('6', 'NTE-2')], max_length=2, verbose_name='Тип приставки абонента')),
                ('serial_number_console', models.CharField(max_length=50, verbose_name='Серийный номер №')),
                ('change_console', models.CharField(choices=[('1', 'NTE-RG-1402F'), ('2', 'NTE-RG-1402G'), ('3', 'NTE-RG-1400F'), ('4', 'NTE-RG-1400G'), ('5', 'NTE-RG-1400'), ('6', 'NTE-2')], max_length=2, verbose_name='Тип подменной приставки')),
                ('serial_number_change_console', models.CharField(max_length=50, verbose_name='Серийный номер №')),
                ('description', models.TextField(max_length=200, verbose_name='Заключение о состоянии оборудования')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.AddConstraint(
            model_name='repair',
            constraint=models.CheckConstraint(check=models.Q(('body__in', ['D', 'S', 'I'])), name='valid_body_state_choice'),
        ),
        migrations.AddConstraint(
            model_name='repair',
            constraint=models.CheckConstraint(check=models.Q(('console__in', ['1', '2', '3', '4', '5', '6'])), name='valid_console_choice'),
        ),
    ]
