# Generated by Django 4.0.6 on 2022-08-01 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console_repair', '0003_alter_repair_options_remove_repair_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='change_console',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='change_repair', to='console_repair.console'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='console',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='console_repair.console'),
        ),
    ]
