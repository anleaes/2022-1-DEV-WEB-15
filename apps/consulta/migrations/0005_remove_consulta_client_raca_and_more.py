# Generated by Django 4.0.5 on 2022-06-15 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0004_consultaraca_consulta_client_raca_consulta_raca_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='client_raca',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='raca_name',
        ),
        migrations.DeleteModel(
            name='ConsultaRaca',
        ),
    ]