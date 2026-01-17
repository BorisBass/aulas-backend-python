# views.py

class TarefaView:
    """View - Responsável pela apresentação"""
    
    def exibir_menu(self):
        """Exibe menu principal"""
        print("\n" + "="*40)
        print("📋 GERENCIADOR DE TAREFAS")
        print("="*40)
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar como concluída")
        print("4. Remover tarefa")
        print("0. Sair")
        print("="*40)
    
    def solicitar_dados_tarefa(self):
        """Coleta dados para nova tarefa"""
        print('#'*30)
        titulo = input("Título da tarefa: ").strip()
        descricao = input("Descrição (opcional): ").strip()
        return titulo, descricao
    
    def exibir_tarefas(self, tarefas):
        """Exibe lista de tarefas"""
        if not tarefas:
            print("📭 Nenhuma tarefa cadastrada!")
            return
        print("\n📋 LISTA DE TAREFAS:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"  {i}. {tarefa}")
    
    def solicitar_indice(self):
        """Solicita índice da tarefa"""
        try:
            indice = int(input("Número da tarefa: ")) - 1
            return indice
        except ValueError:
            return None
    
    def exibir_mensagem(self, mensagem, tipo="info"):
        """Exibe mensagens"""
        if tipo == "erro":
            print(f"❌ {mensagem}")
        elif tipo == "sucesso":
            print(f"✅ {mensagem}")
        else:
            print(f"ℹ️ {mensagem}")




