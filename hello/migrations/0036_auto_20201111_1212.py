# Generated by Django 3.0.8 on 2020-11-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0035_auto_20201110_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='owner_card',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='type_payment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='valute_card',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='published',
            field=models.DateField(auto_now_add=True, db_index=True, null=True, verbose_name='published date'),
        ),
    ]
