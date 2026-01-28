# models.py
class Tarefa:
    """Model - Gerencia dados de uma tarefa"""
    
    def __init__(self, titulo, descricao="", tarefa_id=None, concluida=False, data_criacao=None):
        if not titulo or not titulo.strip():
            raise ValueError("Título é obrigatório")
        self._id = tarefa_id
        self._titulo = titulo.strip()
        self._descricao = descricao.strip()
        self._concluida = concluida
        self._data_criacao = data_criacao
    
    @property
    def id(self):
        """Retorna o ID da tarefa"""
        return self._id
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def descricao(self):
        return self._descricao
    
    @property
    def concluida(self):
        return self._concluida
    
    @property
    def data_criacao(self):
        return self._data_criacao
    
    def marcar_concluida(self):
        """Marca tarefa como concluída"""
        self._concluida = True
    
    def __str__(self):
        status = "✅" if self._concluida else "⏳"
        return f"{status} {self._titulo}"


class TarefaRepository:
    """Gerencia persistência das tarefas usando SQLite"""
    
    def __init__(self, db_manager):
        """
        Inicializa o repositório com gerenciador de banco
        
        Args:
            db_manager: Instância de DatabaseManager
        """
        self.db = db_manager
        self.db.conectar()
    
    def criar(self, tarefa):
        """
        Adiciona nova tarefa no banco de dados
        
        Args:
            tarefa: Instância de Tarefa
            
        Returns:
            ID da tarefa criada
        """
        try:
            cursor = self.db.get_cursor()
            cursor.execute('''
                INSERT INTO tarefas (titulo, descricao, concluida)
                VALUES (?, ?, ?)
            ''', (tarefa.titulo, tarefa.descricao, 1 if tarefa.concluida else 0))
            self.db.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"❌ Erro ao criar tarefa: {e}")
            return None
    
    def listar_todas(self):
        """
        Retorna todas as tarefas do banco
        
        Returns:
            Lista de objetos Tarefa
        """
        try:
            cursor = self.db.get_cursor()
            cursor.execute('''
                SELECT id, titulo, descricao, concluida, data_criacao
                FROM tarefas
                ORDER BY id
            ''')
            resultados = cursor.fetchall()
            
            tarefas = []
            for row in resultados:
                tarefa_id, titulo, descricao, concluida, data_criacao = row
                tarefa = Tarefa(
                    titulo=titulo,
                    descricao=descricao or "",
                    tarefa_id=tarefa_id,
                    concluida=bool(concluida),
                    data_criacao=data_criacao
                )
                tarefas.append(tarefa)
            
            return tarefas
        except Exception as e:
            print(f"❌ Erro ao listar tarefas: {e}")
            return []
    
    def buscar_por_id(self, tarefa_id):
        """
        Busca tarefa por ID
        
        Args:
            tarefa_id: ID da tarefa
            
        Returns:
            Objeto Tarefa ou None se não encontrado
        """
        try:
            cursor = self.db.get_cursor()
            cursor.execute('''
                SELECT id, titulo, descricao, concluida, data_criacao
                FROM tarefas
                WHERE id = ?
            ''', (tarefa_id,))
            row = cursor.fetchone()
            
            if row:
                tarefa_id, titulo, descricao, concluida, data_criacao = row
                return Tarefa(
                    titulo=titulo,
                    descricao=descricao or "",
                    tarefa_id=tarefa_id,
                    concluida=bool(concluida),
                    data_criacao=data_criacao
                )
            return None
        except Exception as e:
            print(f"❌ Erro ao buscar tarefa: {e}")
            return None
    
    def buscar_por_indice(self, indice):
        """
        Busca tarefa por índice na lista (para compatibilidade com versão anterior)
        
        Args:
            indice: Índice na lista (0-based)
            
        Returns:
            Objeto Tarefa ou None se não encontrado
        """
        tarefas = self.listar_todas()
        if 0 <= indice < len(tarefas):
            return tarefas[indice]
        return None
    
    def atualizar(self, tarefa):
        """
        Atualiza uma tarefa no banco
        
        Args:
            tarefa: Objeto Tarefa com ID válido
            
        Returns:
            True se atualizado com sucesso, False caso contrário
        """
        try:
            if not tarefa.id:
                return False
            
            cursor = self.db.get_cursor()
            cursor.execute('''
                UPDATE tarefas
                SET titulo = ?, descricao = ?, concluida = ?
                WHERE id = ?
            ''', (tarefa.titulo, tarefa.descricao, 1 if tarefa.concluida else 0, tarefa.id))
            self.db.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"❌ Erro ao atualizar tarefa: {e}")
            return False
    
    def remover(self, tarefa_id):
        """
        Remove tarefa do banco
        
        Args:
            tarefa_id: ID da tarefa a remover
            
        Returns:
            Objeto Tarefa removido ou None se não encontrado
        """
        try:
            # Buscar tarefa antes de remover
            tarefa = self.buscar_por_id(tarefa_id)
            if not tarefa:
                return None
            
            cursor = self.db.get_cursor()
            cursor.execute('DELETE FROM tarefas WHERE id = ?', (tarefa_id,))
            self.db.connection.commit()
            return tarefa
        except Exception as e:
            print(f"❌ Erro ao remover tarefa: {e}")
            return None















