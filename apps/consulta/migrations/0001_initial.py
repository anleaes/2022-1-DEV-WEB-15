# Generated by Django 3.2.5 on 2022-06-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('animal_name', models.CharField(max_length=100, verbose_name='nomeAnimal')),
                #('raca_name', models.CharField(max_length=100, verbose_name='racaAnimal')),
                ('address', models.CharField(max_length=200, verbose_name='Endereco')),
                ('cell_phone', models.CharField(max_length=20, verbose_name='Telefone celular')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['id'],
            },
        ),
    ]
