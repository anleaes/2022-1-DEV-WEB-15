# Generated by Django 4.0.5 on 2022-06-15 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0015_alter_consulta_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='photo',
        ),
    ]