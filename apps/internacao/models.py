from django.db import models

# Create your models here.
class Internacao(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome do Dono', max_length=50)
    nameAnimal = models.CharField('Nome do Animal', max_length=50)
    date_init = models.DateField('Data De Entrada', auto_now=False, auto_now_add=False) 
    description = models.TextField('Descricao', max_length=100)
    doc = models.FileField('Documentos', upload_to='docs')
    
    class Meta:
        verbose_name = 'Internacao'
        verbose_name_plural = 'Internacoes'
        ordering =['id']

    def __str__(self):
        return self.name
