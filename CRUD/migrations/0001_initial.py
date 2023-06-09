# Generated by Django 4.2 on 2023-05-09 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_habitacion', models.PositiveIntegerField(unique=True)),
                ('capacidad', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'habitacion',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_paciente', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=20)),
                ('habitacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pacientes', to='CRUD.habitacion')),
            ],
            options={
                'db_table': 'paciente',
            },
        ),
        migrations.CreateModel(
            name='Piso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_piso', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'piso',
            },
        ),
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_visitante', models.PositiveIntegerField()),
                ('rostro', models.CharField(blank=True, max_length=99, null=True)),
                ('foto', models.CharField(blank=True, max_length=99, null=True)),
                ('estado', models.CharField(max_length=20)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitantes', to='CRUD.habitacion')),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visitantes', to='CRUD.paciente')),
            ],
            options={
                'db_table': 'visitante',
            },
        ),
        migrations.AddField(
            model_name='habitacion',
            name='piso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habitaciones', to='CRUD.piso'),
        ),
    ]
