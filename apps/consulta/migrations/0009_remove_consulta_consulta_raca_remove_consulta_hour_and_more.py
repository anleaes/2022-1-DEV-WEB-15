# Generated by Django 4.0.5 on 2022-06-15 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0008_alter_consulta_raca_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='consulta_raca',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='raca_name',
        ),
        migrations.DeleteModel(
            name='ConsultaRaca',
        ),
    ]
