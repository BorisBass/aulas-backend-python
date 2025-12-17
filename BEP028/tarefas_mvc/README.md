# Sistema de Gerenciamento de Tarefas - MVC

Exemplo prático de implementação do padrão MVC (Model-View-Controller) em Python.

## 📁 Estrutura do Projeto

```
tarefas_mvc/
├── models.py      # Model: Tarefa e TarefaRepository
├── views.py       # View: TarefaView
├── controllers.py # Controller: TarefaController
├── main.py        # Ponto de entrada do sistema
└── README.md      # Este arquivo
```

## 🚀 Como Executar

### Opção 1: Execução direta (recomendado)

Navegue até a pasta `tarefas_mvc` e execute:

```bash
cd BEP028/tarefas_mvc
python3 main.py
```

ou no Windows:

```bash
cd BEP028\tarefas_mvc
python main.py
```

### Opção 2: Execução como módulo

A partir da raiz do projeto `aulas`:

```bash
python3 -m BEP028.tarefas_mvc.main
```

ou no Windows:

```bash
python -m BEP028.tarefas_mvc.main
```

## 📋 Funcionalidades

O sistema permite:

1. **Criar tarefa** - Adiciona uma nova tarefa com título e descrição
2. **Listar tarefas** - Mostra todas as tarefas cadastradas
3. **Marcar como concluída** - Marca uma tarefa como concluída
4. **Remover tarefa** - Remove uma tarefa do sistema

## 🎯 Padrão MVC

Este exemplo demonstra a separação de responsabilidades do padrão MVC:

- **Model** (`models.py`): Gerencia os dados e a lógica de negócio
  - `Tarefa`: Representa uma tarefa individual
  - `TarefaRepository`: Gerencia a persistência das tarefas

- **View** (`views.py`): Responsável pela apresentação
  - `TarefaView`: Exibe menus, coleta dados do usuário e mostra mensagens

- **Controller** (`controllers.py`): Coordena Model e View
  - `TarefaController`: Processa ações do usuário e coordena a comunicação entre Model e View

## 💡 Exemplo de Uso

```
========================================
📋 GERENCIADOR DE TAREFAS
========================================
1. Criar tarefa
2. Listar tarefas
3. Marcar como concluída
4. Remover tarefa
0. Sair
========================================
👉 Escolha: 1
Título da tarefa: Estudar Python
Descrição (opcional): Revisar conceitos de POO
✅ Tarefa criada!
```

## 📚 Observações

- Este é um exemplo didático que armazena dados em memória (lista)
- Os dados são perdidos quando o programa é encerrado
- Para persistência permanente, seria necessário integrar com banco de dados (como no exemplo do CRUD refatorado)

