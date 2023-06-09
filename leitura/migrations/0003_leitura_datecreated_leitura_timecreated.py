# Generated by Django 4.1.7 on 2023-04-01 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leitura', '0002_remove_leitura_dispositivo_leitura_mac'),
    ]

    operations = [
        migrations.AddField(
            model_name='leitura',
            name='dateCreated',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leitura',
            name='timeCreated',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
