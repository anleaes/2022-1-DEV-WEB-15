# Generated by Django 4.0.5 on 2022-06-15 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('racas', '0001_initial'),
        ('consulta', '0003_raca'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaRaca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Raca item',
                'verbose_name_plural': 'Raca item',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='consulta',
            name='client_raca',
            field=models.ManyToManyField(blank=True, through='consulta.ConsultaRaca', to='racas.raca'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='raca_name',
            field=models.CharField(default='Cachorro', max_length=100, verbose_name='racaAnimal'),
        ),
        migrations.DeleteModel(
            name='Raca',
        ),
        migrations.AddField(
            model_name='consultaraca',
            name='consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.consulta'),
        ),
        migrations.AddField(
            model_name='consultaraca',
            name='raca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racas.raca'),
        ),
    ]
