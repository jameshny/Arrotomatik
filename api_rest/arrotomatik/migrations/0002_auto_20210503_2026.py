# Generated by Django 3.2 on 2021-05-03 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrotomatik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airinformation',
            name='humidity',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='airinformation',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='earthhumidity',
            name='humidity',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
