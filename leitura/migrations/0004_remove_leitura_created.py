# Generated by Django 4.1.7 on 2023-04-01 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leitura', '0003_leitura_datecreated_leitura_timecreated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leitura',
            name='created',
        ),
    ]
