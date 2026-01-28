# main.py
from database import DatabaseManager
from models import TarefaRepository
from views import TarefaView
from controllers import TarefaController

if __name__ == "__main__":
    # Inicializa componentes seguindo padrão MVC
    db_manager = DatabaseManager('tarefas.db')
    repository = TarefaRepository(db_manager)
    view = TarefaView()
    controller = TarefaController(repository, view)
    
    try:
        controller.iniciar()
    finally:
        # Garante que a conexão seja fechada
        db_manager.fechar()















