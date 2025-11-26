"""
Sistema CRUD de Gerenciamento de Alunos
Módulo organizado para demonstrar boas práticas de estruturação de projetos Python
"""

__version__ = "1.0.0"
__author__ = "BEP-016"

# Importações principais para facilitar uso
from .database import conectar_banco, fechar_conexao
from .crud_operations import (
    cadastrar_aluno,
    listar_alunos,
    buscar_aluno,
    atualizar_aluno,
    remover_aluno,
    mostrar_estatisticas
)
from .menu import exibir_menu

__all__ = [
    'conectar_banco',
    'fechar_conexao',
    'cadastrar_aluno',
    'listar_alunos',
    'buscar_aluno',
    'atualizar_aluno',
    'remover_aluno',
    'mostrar_estatisticas',
    'exibir_menu'
]

