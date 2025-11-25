"""
Programa Principal - Sistema CRUD de Gerenciamento de Alunos
Este é o ponto de entrada do sistema, orquestra todas as operações
"""

from .database import conectar_banco, fechar_conexao
from .menu import exibir_menu
from .crud_operations import (
    cadastrar_aluno,
    listar_alunos,
    buscar_aluno,
    atualizar_aluno,
    remover_aluno,
    mostrar_estatisticas
)


def main():
    """Função principal do programa"""
    print("🚀 Iniciando Sistema de Gerenciamento de Alunos...")
    
    # Conectar ao banco
    conn, cursor = conectar_banco()
    if not conn:
        print("❌ Não foi possível conectar ao banco. Encerrando...")
        return
    
    try:
        while True:
            exibir_menu()
            opcao = input("👉 Escolha uma opção: ").strip()
            
            if opcao == '1':
                cadastrar_aluno(cursor, conn)
            elif opcao == '2':
                listar_alunos(cursor)
            elif opcao == '3':
                buscar_aluno(cursor)
            elif opcao == '4':
                atualizar_aluno(cursor, conn)
            elif opcao == '5':
                remover_aluno(cursor, conn)
            elif opcao == '6':
                mostrar_estatisticas(cursor)
            elif opcao == '0':
                print("\n👋 Obrigado por usar o sistema! Até logo!")
                break
            else:
                print("❌ Opção inválida! Tente novamente.")
            
            input("\n⏸️ Pressione Enter para continuar...")
    
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
    finally:
        # Sempre fechar a conexão
        fechar_conexao(conn)


# Executar o programa quando rodado diretamente
if __name__ == "__main__":
    main()

