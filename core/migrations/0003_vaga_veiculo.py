# Generated by Django 3.0.6 on 2020-05-09 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200509_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='veiculo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Veiculo'),
        ),
    ]
