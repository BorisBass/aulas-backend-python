# models.py
class Tarefa:
    """Model - Gerencia dados de uma tarefa"""
    
    def __init__(self, titulo, descricao=""):
        if not titulo or not titulo.strip():
            raise ValueError("Título é obrigatório")
        self._titulo = titulo.strip()
        self._descricao = descricao.strip()
        self._concluida = False
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def descricao(self):
        return self._descricao
    
    @property
    def concluida(self):
        return self._concluida
    
    def marcar_concluida(self):
        """Marca tarefa como concluída"""
        self._concluida = True
    
    def __str__(self):
        status = "✅" if self._concluida else "⏳"
        return f"{status} {self._titulo}"


class TarefaRepository:
    """Gerencia persistência das tarefas"""
    
    def __init__(self):
        self._tarefas = []
        self._proximo_id = 1
    
    def criar(self, tarefa):
        """Adiciona nova tarefa"""
        self._tarefas.append(tarefa)
        return len(self._tarefas) - 1
    
    def listar_todas(self):
        """Retorna todas as tarefas"""
        return self._tarefas.copy()
    
    def buscar_por_indice(self, indice):
        """Busca tarefa por índice"""
        if 0 <= indice < len(self._tarefas):
            return self._tarefas[indice]
        return None
    
    def remover(self, indice):
        """Remove tarefa"""
        if 0 <= indice < len(self._tarefas):
            return self._tarefas.pop(indice)
        return None