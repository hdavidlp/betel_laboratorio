# Generated by Django 4.0.3 on 2022-04-11 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_ordentrabajo'),
    ]

    operations = [
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
                ('ot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ordentrabajo')),
            ],
        ),
    ]
