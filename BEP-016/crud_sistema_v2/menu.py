"""
Módulo de Interface do Menu
Aplica conceitos de BEP-017, BEP-018: Classes, Métodos
"""

from typing import List
from .models import Aluno


class Menu:
    """
    Classe responsável pela interface do usuário
    Aplica: Classes, Encapsulamento
    """
    
    @staticmethod
    def exibir_menu_principal():
        """Exibe o menu principal do sistema"""
        print("\n" + "="*50)
        print("🎓 SISTEMA DE GERENCIAMENTO DE ALUNOS (Versão OO)")
        print("="*50)
        print("1. 📝 Cadastrar novo aluno")
        print("2. 📋 Listar todos os alunos")
        print("3. 🔍 Buscar aluno por nome")
        print("4. ✏️ Atualizar dados do aluno")
        print("5. 🗑️ Remover aluno")
        print("6. 📊 Estatísticas")
        print("0. 🚪 Sair")
        print("="*50)
    
    @staticmethod
    def exibir_cabecalho(titulo: str, largura: int = 30):
        """
        Exibe um cabeçalho formatado
        
        Args:
            titulo: Título a ser exibido
            largura: Largura da linha separadora
        """
        print(f"\n{titulo}")
        print("-" * largura)
    
    @staticmethod
    def formatar_aluno(aluno: Aluno) -> str:
        """
        Formata os dados de um aluno para exibição
        
        Args:
            aluno: Objeto Aluno
        
        Returns:
            String formatada com dados do aluno
        """
        idade_str = str(aluno.idade) if aluno.idade else "N/A"
        curso_str = aluno.curso if aluno.curso else "N/A"
        nota_str = f"{aluno.nota:.1f}" if aluno.nota else "N/A"
        
        return (f"{aluno.id:<3} {aluno.nome:<25} {idade_str:<5} "
                f"{curso_str:<15} {nota_str:<5} {aluno.data_cadastro}")
    
    @staticmethod
    def exibir_lista_alunos(alunos: List[Aluno], titulo: str = "LISTA DE ALUNOS"):
        """
        Exibe uma lista de alunos formatada
        
        Args:
            alunos: Lista de objetos Aluno
            titulo: Título da lista
        """
        if not alunos:
            print("📭 Nenhum aluno encontrado!")
            return
        
        print(f"\n📋 {titulo} ({len(alunos)} encontrado(s))")
        print("-" * 90)
        print(f"{'ID':<3} {'Nome':<25} {'Idade':<5} {'Curso':<15} {'Nota':<5} {'Data'}")
        print("-" * 90)
        
        for aluno in alunos:
            print(Menu.formatar_aluno(aluno))
    
    @staticmethod
    def exibir_estatisticas(stats: dict):
        """
        Exibe estatísticas formatadas
        
        Args:
            stats: Dicionário com estatísticas
        """
        print(f"\n👥 Total de alunos: {stats['total']}")
        
        if stats['total'] == 0:
            print("📭 Nenhum aluno cadastrado para estatísticas!")
            return
        
        if stats['por_curso']:
            print(f"\n📚 Alunos por curso:")
            for curso, qtd in stats['por_curso'].items():
                print(f"  {curso}: {qtd} aluno(s)")
        
        if stats['media_notas']:
            print(f"\n📈 Média das notas: {stats['media_notas']:.2f}")
        
        print(f"\n📅 Cadastrados hoje: {stats['cadastrados_hoje']}")
        
        if stats['melhor_nota']:
            melhor = stats['melhor_nota']
            print(f"\n🏆 Melhor nota: {melhor['nota']:.1f} - {melhor['aluno']}")

