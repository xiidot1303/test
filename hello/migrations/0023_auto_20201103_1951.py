# Generated by Django 3.0.8 on 2020-11-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0022_auto_20201103_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='day_payment',
            field=models.DateField(blank=True, verbose_name='Дата оплата'),
        ),
    ]
