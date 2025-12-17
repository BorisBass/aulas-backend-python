# controllers.py
from models import Tarefa, TarefaRepository
from views import TarefaView

class TarefaController:
    """Controller - Coordena Model e View"""
    
    def __init__(self):
        self.repository = TarefaRepository()
        self.view = TarefaView()
    
    def iniciar(self):
        """Inicia o sistema"""
        while True:
            self.view.exibir_menu()
            opcao = input("👉 Escolha: ").strip()
            
            if opcao == '1':
                self.criar_tarefa()
            elif opcao == '2':
                self.listar_tarefas()
            elif opcao == '3':
                self.marcar_concluida()
            elif opcao == '4':
                self.remover_tarefa()
            elif opcao == '0':
                break
            else:
                self.view.exibir_mensagem("Opção inválida!", "erro")
    
    def criar_tarefa(self):
        """Processa criação de tarefa"""
        try:
            titulo, descricao = self.view.solicitar_dados_tarefa()
            tarefa = Tarefa(titulo, descricao)
            self.repository.criar(tarefa)
            self.view.exibir_mensagem("Tarefa criada!", "sucesso")
        except ValueError as e:
            self.view.exibir_mensagem(str(e), "erro")
    
    def listar_tarefas(self):
        """Lista todas as tarefas"""
        tarefas = self.repository.listar_todas()
        self.view.exibir_tarefas(tarefas)
    
    def marcar_concluida(self):
        """Marca tarefa como concluída"""
        tarefas = self.repository.listar_todas()
        self.view.exibir_tarefas(tarefas)
        indice = self.view.solicitar_indice()
        tarefa = self.repository.buscar_por_indice(indice)
        if tarefa:
            tarefa.marcar_concluida()
            self.view.exibir_mensagem("Tarefa concluída!", "sucesso")
        else:
            self.view.exibir_mensagem("Tarefa não encontrada!", "erro")
    
    def remover_tarefa(self):
        """Remove tarefa"""
        tarefas = self.repository.listar_todas()
        self.view.exibir_tarefas(tarefas)
        indice = self.view.solicitar_indice()
        tarefa = self.repository.remover(indice)
        if tarefa:
            self.view.exibir_mensagem("Tarefa removida!", "sucesso")
        else:
            self.view.exibir_mensagem("Tarefa não encontrada!", "erro")
