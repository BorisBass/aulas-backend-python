from django import forms
from django.core.exceptions import ValidationError
from .models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'prioridade', 'status', 'concluida']
        # não incluir: usuario (definido na view), criado_em (automático)
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'prioridade': 'Prioridade',
            'status': 'Status (%)',
            'concluida': 'Concluída',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Estudar Django'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'prioridade': forms.Select(choices=[('alta', 'Alta'), ('media', 'Média'), ('baixa', 'Baixa')], attrs={'class': 'form-control'}),
            'status': forms.NumberInput(attrs={'min': 0, 'max': 100, 'class': 'form-control'}),
            'concluida': forms.CheckboxInput(),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if titulo and len(titulo.strip()) < 3:
            raise ValidationError('O título deve ter pelo menos 3 caracteres.')
        return titulo.strip() if titulo else titulo