from django.db import models
from django.utils import timezone
from titulo.models import Titulo #somente a classe inteira pode ser importada não so um campo em especifico

# Create your models here.

class Instrutor(models.Model): # é a "planta" do objeto
    id = models.AutoField(primary_key=True, 
                          help_text='Id do instrutor')
    rg = models.CharField(max_length=15, 
                                 help_text='Rg do instrutor')
    nome = models.CharField(max_length=70, 
                                 help_text='Nome do instrutor')
    dataNascimento = models.DateField(null=True,
                                      blank=True,
                                      default=timezone.now(),
                                      help_text='Data de nascimento do instrutor')
    telefone = models.CharField(max_length=9, 
                                 help_text='Telefone do instrutor')
    ddd = models.CharField(max_length=3, 
                                 help_text='DDD do telefone do instrutor')
    codigo_titulo = models.ForeignKey(Titulo, null=True, blank=True,
                                      related_name='titulos',
                                      on_delete=models.SET_NULL,#Se você deletar o titulo o instrutor recebe null 
                                      db_column='titulo_codigo')#Aplica o nome da coluna da tabela original nesta coluna
    
    def __str__(self):
        return f'{self.nome} - {self.id}'