# Generated by Django 4.0.3 on 2022-04-15 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0017_remove_ordentrabajo_cargo_remove_ordentrabajo_medico_and_more'),
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('secuencia', models.SmallIntegerField()),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.cargo')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='BaseResultados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAnalisis', models.IntegerField()),
                ('nombre_Anlisis', models.CharField(max_length=120)),
                ('prueba', models.CharField(max_length=50)),
                ('resultado', models.TextField(blank=True, null=True)),
                ('udm', models.CharField(blank=True, max_length=20, null=True)),
                ('minimo', models.CharField(blank=True, max_length=10, null=True)),
                ('maximo', models.CharField(blank=True, max_length=10, null=True)),
                ('tipo', models.CharField(max_length=10)),
                ('fuera_rango', models.CharField(max_length=20)),
                ('nota_Encabezado_Analisis', models.TextField(blank=True, null=True)),
                ('nota_Pie_Analisis', models.TextField(blank=True, null=True)),
                ('agrupador1', models.TextField(blank=True, null=True)),
                ('nota_Encabezado_Agrupador1', models.TextField(blank=True, null=True)),
                ('nota_Pie_Agrupador1', models.TextField(blank=True, null=True)),
                ('agrupador2', models.TextField(blank=True, null=True)),
                ('nota_Encabezado_Agrupador2', models.TextField(blank=True, null=True)),
                ('nota_Pie_Agrupador2', models.TextField(blank=True, null=True)),
                ('nota_Prueba', models.TextField(blank=True, null=True)),
                ('ot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ots.ordentrabajo')),
            ],
        ),
    ]
