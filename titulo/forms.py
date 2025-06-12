from django import forms

#classe formulario inclusao
class TituloForm(forms.Form):
    descricao = forms.CharField(max_length=70,
                                required=True, 
                                 help_text='informe a descrição do titulo')