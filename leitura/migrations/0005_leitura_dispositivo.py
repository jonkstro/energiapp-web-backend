# Generated by Django 4.1.7 on 2023-03-30 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0003_alter_dispositivo_user'),
        ('leitura', '0004_remove_leitura_dispositivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='leitura',
            name='dispositivo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dispositivo.dispositivo'),
            preserve_default=False,
        ),
    ]