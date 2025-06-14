from django import forms

class TiposDeAtividadeForm(forms.Form):
    descricao = forms.CharField(max_length=100, 
                                 help_text='informe a descrição do Tipo de Atividade')