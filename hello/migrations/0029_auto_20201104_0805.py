# Generated by Django 3.0.8 on 2020-11-04 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0028_auto_20201104_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='t'),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field = models.CharField(max_length=50, blank=True, verbose_name="name"),
            
        ),
    ]
