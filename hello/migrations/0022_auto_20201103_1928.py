# Generated by Django 3.0.8 on 2020-11-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0021_account_pse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pseudonym',
            field=models.CharField(max_length=40, null=True, verbose_name='Псевдоним'),
        ),
    ]
