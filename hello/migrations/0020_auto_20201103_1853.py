# Generated by Django 3.0.8 on 2020-11-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0019_auto_20201103_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pseudonym',
            field=models.CharField(choices=[('lala', 'opop'), ('dsasda', 'faffa')], max_length=40, null=True, verbose_name='Псевдоним'),
        ),
    ]
