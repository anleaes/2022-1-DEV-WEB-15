# Generated by Django 4.0.5 on 2022-06-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0013_consultaraca_consulta_consulta_raca_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='photo',
            field=models.ImageField(default='null', upload_to='photos', verbose_name='Foto'),
        ),
    ]
