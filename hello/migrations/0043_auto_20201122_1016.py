# Generated by Django 3.0.8 on 2020-11-22 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0042_stories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acc_pre_value',
            name='pse',
        ),
        migrations.RemoveField(
            model_name='account',
            name='pse',
        ),
        migrations.AddField(
            model_name='stories',
            name='obj_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
