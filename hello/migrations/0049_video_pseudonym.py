# Generated by Django 3.1.7 on 2021-04-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0048_audio_pseudonym'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='pseudonym',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
