# Generated by Django 5.0.6 on 2024-05-14 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_cliente_cuit_cliente_dni_cuit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
