# Generated by Django 4.0.3 on 2022-04-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_rango'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='udm',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]