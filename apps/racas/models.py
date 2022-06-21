from django.db import models

# Create your models here.

class Raca(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    
    class Meta:
        verbose_name = 'Raca'
        verbose_name_plural = 'Raca'
        ordering =['id']

    def __str__(self):
        return self.name