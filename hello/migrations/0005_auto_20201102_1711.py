# Generated by Django 3.0.8 on 2020-11-02 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20201102_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='hello.Status', verbose_name='Статус'),
        ),
    ]
