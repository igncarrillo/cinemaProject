# Generated by Django 3.1.4 on 2021-01-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_auto_20210121_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='genero',
            field=models.CharField(max_length=30),
        ),
    ]
