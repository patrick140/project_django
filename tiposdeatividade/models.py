from django.db import models

# Create your models here.

class tiposDeAtividade(models.Model):
    codigo = models.AutoField(primary_key=True,
                              help_text='codigo do Tipo de Atividade')
    descricao = models.CharField(max_length=100, 
                                 help_text='informe a descrição do Tipo de Atividade')
    
    def __str__(self):
        return f'{self.codigo} - {self.descricao}'
