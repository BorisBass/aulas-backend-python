"""
Módulo de Interface do Menu
Responsável por: exibição de menus e interfaces do usuário
"""


def exibir_menu() -> None:
    """Exibe o menu principal do sistema"""
    print("\n" + "="*50)
    print("🎓 SISTEMA DE GERENCIAMENTO DE ALUNOS")
    print("="*50)
    print("1. 📝 Cadastrar novo aluno")
    print("2. 📋 Listar todos os alunos")
    print("3. 🔍 Buscar aluno por nome")
    print("4. ✏️ Atualizar dados do aluno")
    print("5. 🗑️ Remover aluno")
    print("6. 📊 Estatísticas")
    print("0. 🚪 Sair")
    print("="*50)


def exibir_cabecalho(titulo: str, largura: int = 30) -> None:
    """
    Exibe um cabeçalho formatado
    
    Args:
        titulo: Título a ser exibido
        largura: Largura da linha separadora
    """
    print(f"\n{titulo}")
    print("-" * largura)


def formatar_aluno(aluno: tuple) -> str:
    """
    Formata os dados de um aluno para exibição
    
    Args:
        aluno: Tupla com dados do aluno (id, nome, idade, curso, nota, data)
    
    Returns:
        String formatada com dados do aluno
    """
    id_aluno, nome, idade, curso, nota, data = aluno
    idade_display = idade if idade else "N/A"
    curso_display = curso if curso else "N/A"
    nota_display = f"{nota:.1f}" if nota else "N/A"
    return f"{id_aluno:<3} {nome:<25} {idade_display:<5} {curso_display:<15} {nota_display:<5} {data}"

