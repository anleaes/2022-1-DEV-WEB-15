from email.policy import default
from django.db import models
from racas.models import Raca

# Create your models here.
class Consulta(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    animal_name = models.CharField('nomeAnimal', max_length=100)
    photo = models.ImageField('Foto', upload_to='photos')
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    HOUR_CHOICES = (
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
    )
    hour = models.CharField('Horario', max_length=5, choices=HOUR_CHOICES, default="09:00")
    consulta_raca = models.ManyToManyField(Raca, through='ConsultaRaca', blank=True)
    
    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering =['id']

    def __str__(self):
        return self.first_name


class ConsultaRaca(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Raça'
        verbose_name_plural = 'Raças'
        ordering =['id']

    def __str__(self):
        return self.raca.name