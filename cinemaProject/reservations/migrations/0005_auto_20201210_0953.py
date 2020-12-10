# Generated by Django 3.1.4 on 2020-12-10 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20201208_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='asiento',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='sala',
            name='fila',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]