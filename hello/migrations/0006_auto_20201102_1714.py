# Generated by Django 3.0.8 on 2020-11-02 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_auto_20201102_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='s',
            field=models.CharField(db_index=True, max_length=20, null=True, unique=True),
        ),
    ]