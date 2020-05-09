# Generated by Django 3.0.6 on 2020-05-09 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=16)),
                ('cap_max', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('CARRO', 'Carro'), ('MOTO', 'Moto')], max_length=6)),
                ('nome', models.CharField(max_length=10)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=16)),
                ('ocupada', models.BooleanField(default=False)),
                ('estacionamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estacionamento')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroEstacionamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField(auto_now=True)),
                ('data_saida', models.DateField(blank=True, null=True)),
                ('estacionamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Estacionamento')),
                ('veiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Veiculo')),
            ],
        ),
    ]
