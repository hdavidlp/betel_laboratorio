# Generated by Django 4.0.3 on 2022-04-15 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ots', '0004_ordentrabajo_cargo_ordentrabajo_medico_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseresultados',
            name='ot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ots.ordentrabajo'),
        ),
    ]