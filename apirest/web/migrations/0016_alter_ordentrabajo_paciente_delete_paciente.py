# Generated by Django 4.0.3 on 2022-04-15 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
        ('web', '0015_baseresultados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordentrabajo',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente'),
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
    ]
