# core/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Tarefa

class TarefaForm(forms.Form):
    descricao = forms.CharField(
        max_length=200,
        required=True,
        label='Descrição',
        help_text='Informe a tarefa. Ex. Estudar Django',
        widget=forms.TextInput(attrs={'class': 'form-control'}
)
    )
    prioridade = forms.ChoiceField(
        choices=[('alta', 'Alta'), ('media', 'Média'), ('baixa', 'Baixa')],
        label='Prioridade',
        help_text='Escolha a prioridade',

    )
    status = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=0,
        label='Status (%)'
    )
#    data_inicio = forms.DateField()
#    data_fim = forms.DateField()

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if descricao and len(descricao.strip()) < 5:
            raise ValidationError('A descrição deve ter pelo menos 5 caracteres.')
        
        if Tarefa.objects.filter(descricao=descricao).exists():
            raise ValidationError('Esta tarefa já está cadastrada.')
        
        return descricao.strip()  # remove espaços extras e retorna    


    
#    def clean(self):
#        cleaned_data = super().clean()  # chama limpeza padrão
#
#        descricao = self.cleaned_data.get('descricao')
#        data_inicio = cleaned_data.get('data_inicio')
#        data_fim = cleaned_data.get('data_fim')
#
#        # validação que envolve múltiplos campos
#
#        if descricao and len(descricao.strip()) < 5:
#            raise ValidationError('A descrição deve ter pelo menos 5 caracteres.')
#        
#        if Tarefa.objects.filter(descricao=descricao).exists():
#            raise ValidationError('Esta tarefa já está cadastrada.')        
#
#        if data_inicio and data_fim:
#            if data_fim < data_inicio:
#                raise ValidationError({
#                    'data_fim': 'A data de fim deve ser posterior à data de início.'
#                })
#        
#        return cleaned_data  # retorna todos os dados limpos        