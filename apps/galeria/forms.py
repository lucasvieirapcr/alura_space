from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):     #forms.ModelForm: criando a partir de um model pre existente
    class Meta:     #ela diz respeito aos metadados da minha propria classe
        model = Fotografia
        exclude = ['publicada',] #nele vamos indicar os inputs que não queremos exibidos

        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control'}),
            'legenda' : forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%y',
                attrs={
                    'type':'date',
                    'class': 'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }

