# Generated by Django 3.0.8 on 2020-11-03 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0020_auto_20201103_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='pse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='hello.Profile'),
        ),
    ]
