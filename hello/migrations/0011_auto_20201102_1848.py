# Generated by Django 3.0.8 on 2020-11-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0010_auto_20201102_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.CharField(max_length=30, null=True, verbose_name='Номер телефона'),
        ),
    ]
