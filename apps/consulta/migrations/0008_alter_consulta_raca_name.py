# Generated by Django 4.0.5 on 2022-06-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0007_consulta_consulta_raca_consulta_hour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='raca_name',
            field=models.CharField(default='Golden', max_length=100, verbose_name='racaAnimal'),
        ),
    ]
