# Generated by Django 4.1.7 on 2023-03-29 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='latitude',
            field=models.DecimalField(decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='longitude',
            field=models.DecimalField(decimal_places=3, max_digits=8, null=True),
        ),
    ]
