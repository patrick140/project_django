from django import forms


class InstrutorForm(forms.Form):
    nome = forms.CharField(max_length=70, 
                                 help_text='Nome do instrutor')
    rg = forms.CharField(max_length=15, 
                                 help_text='Rg do instrutor')
    dataNascimento = forms.DateField(
                                      help_text='Data de nascimento do instrutor')
    telefone = forms.CharField(max_length=9, 
                                 help_text='Telefone do instrutor')
    ddd = forms.CharField(max_length=3, 
                                 help_text='DDD do telefone do instrutor')
    codigo_titulo = forms.CharField(max_length=70, 
                                 help_text='informe a descrição do titulo')