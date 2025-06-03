from django.db import models

# Create your models here.

class Titulo(models.Model):
    codigo = models.AutoField(primary_key=True,
                              help_text='codigo do Titulo')
    descricao = models.CharField(max_length=70, 
                                 help_text='informe a descrição do titulo')
    
    def __str__(self):
        return f'{self.codigo} - {self.descricao}'
