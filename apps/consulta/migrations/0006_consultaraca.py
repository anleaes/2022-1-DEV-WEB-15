# Generated by Django 4.0.5 on 2022-06-15 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('racas', '0001_initial'),
        ('consulta', '0005_remove_consulta_client_raca_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaRaca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.consulta')),
                ('raca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racas.raca')),
            ],
            options={
                'verbose_name': 'Raça',
                'verbose_name_plural': 'Raças',
                'ordering': ['id'],
            },
        ),
    ]
