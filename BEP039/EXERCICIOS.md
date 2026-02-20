## Exercícios - BEP039: Formulários e Validação de Dados

### Exercício 1: Criar Form básico
Crie um arquivo `core/forms.py` com um formulário `TarefaForm` contendo:
- `descricao` (CharField, max_length=200, obrigatório)
- `prioridade` (ChoiceField com opções: alta, média, baixa)
- `status` (IntegerField, min_value=0, max_value=100, inicial=0)

### Exercício 2: View com formulário
Crie uma view `criar_tarefa` que:
- Exibe o formulário vazio no GET
- Processa o formulário no POST
- Valida os dados com `is_valid()`
- Salva a tarefa no banco se válido
- Redireciona para a lista após salvar
- Reexibe o formulário com erros se inválido

### Exercício 3: Validação customizada
Adicione validação no `TarefaForm`:
- `clean_descricao()`: Verifica se a descrição tem pelo menos 5 caracteres (sem contar espaços)
- Retorna a descrição sem espaços extras (usando `strip()`)

### Exercício 4: Template com erros
Crie um template `criar_tarefa.html` que:
- Exibe o formulário usando `{{ form.as_p }}`
- Inclui `{% csrf_token %}`
- Mostra erros de validação (já incluídos no `as_p`)
- Tem um botão de submit

### Exercício 5: Validação entre campos
Crie um formulário `EventoForm` com:
- `data_inicio` (DateField)
- `data_fim` (DateField)
- Implemente `clean()` para verificar se `data_fim` é posterior a `data_inicio`
- Exiba erro específico no campo `data_fim` se inválido

### Exercício 6: Template customizado
Modifique o template para usar um loop `{% for field in form %}`:
- Exiba label, campo e erros de cada campo
- Adicione estilos CSS para destacar erros em vermelho
- Mostre `help_text` se disponível
