"""
Módulo de Repositório (Padrão Repository)
Aplica conceitos de BEP-017, BEP-018, BEP-021: Classes, Composição
"""

from typing import List, Optional
from .models import Aluno
from .database import DatabaseManager
from .exceptions import AlunoNaoEncontradoError, ErroBancoDados


class AlunoRepository:
    """
    Classe responsável pelas operações CRUD no banco de dados
    Aplica: Classes, Composição (tem DatabaseManager), Encapsulamento
    """
    
    def __init__(self, db_manager: DatabaseManager):
        """
        Inicializa o repositório com um gerenciador de banco
        
        Args:
            db_manager: Instância de DatabaseManager (Composição)
        """
        self._db_manager = db_manager
    
    def criar(self, aluno: Aluno) -> Aluno:
        """
        Cria um novo aluno no banco de dados
        
        Args:
            aluno: Objeto Aluno a ser criado
        
        Returns:
            Aluno criado com ID atribuído
        
        Raises:
            ErroBancoDados: Se houver erro no banco
        """
        try:
            with self._db_manager.get_cursor() as cursor:
                cursor.execute('''
                    INSERT INTO alunos (nome, idade, curso, nota)
                    VALUES (?, ?, ?, ?)
                ''', aluno.to_tuple())
                
                # Obter ID gerado
                aluno_id = cursor.lastrowid
                
                # Buscar aluno completo
                return self.buscar_por_id(aluno_id)
        except Exception as e:
            if isinstance(e, ErroBancoDados):
                raise
            raise ErroBancoDados("criar aluno", e)
    
    def buscar_por_id(self, aluno_id: int) -> Aluno:
        """
        Busca um aluno pelo ID
        
        Args:
            aluno_id: ID do aluno
        
        Returns:
            Objeto Aluno encontrado
        
        Raises:
            AlunoNaoEncontradoError: Se aluno não for encontrado
            ErroBancoDados: Se houver erro no banco
        """
        try:
            with self._db_manager.get_cursor() as cursor:
                cursor.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,))
                resultado = cursor.fetchone()
                
                if not resultado:
                    raise AlunoNaoEncontradoError(aluno_id=aluno_id)
                
                return Aluno.from_tuple(resultado)
        except AlunoNaoEncontradoError:
            raise
        except Exception as e:
            if isinstance(e, ErroBancoDados):
                raise
            raise ErroBancoDados("buscar aluno", e)
    
    def buscar_por_nome(self, nome: str) -> List[Aluno]:
        """
        Busca alunos por nome (usando LIKE)
        
        Args:
            nome: Nome ou parte do nome para buscar
        
        Returns:
            Lista de alunos encontrados
        
        Raises:
            ErroBancoDados: Se houver erro no banco
        """
        try:
            with self._db_manager.get_cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM alunos WHERE nome LIKE ? ORDER BY nome",
                    (f"%{nome}%",)
                )
                resultados = cursor.fetchall()
                
                return [Aluno.from_tuple(row) for row in resultados]
        except Exception as e:
            if isinstance(e, ErroBancoDados):
                raise
            raise ErroBancoDados("buscar alunos por nome", e)
    
    def listar_todos(self) -> List[Aluno]:
        """
        Lista todos os alunos cadastrados
        
        Returns:
            Lista de todos os alunos
        
        Raises:
            ErroBancoDados: Se houver erro no banco
        """
        try:
            with self._db_manager.get_cursor() as cursor:
                cursor.execute("SELECT * FROM alunos ORDER BY nome")
                resultados = cursor.fetchall()
                
                return [Aluno.from_tuple(row) for row in resultados]
        except Exception as e:
            if isinstance(e, ErroBancoDados):
                raise
            raise ErroBancoDados("listar alunos", e)
    
    def atualizar(self, aluno: Aluno) -> Aluno:
        """
        Atualiza um aluno existente
        
        Args:
            aluno: Objeto Aluno com dados atualizados (deve ter ID)
        
        Returns:
            Aluno atualizado
        
        Raises:
            AlunoNaoEncontradoError: Se aluno não for encontrado
            ErroBancoDados: Se houver erro no banco
        """
        if not aluno.id:
            raise ValueError("Aluno deve ter ID para ser atualizado")
        
        try:
            # Verificar se existe
            self.buscar_por_id(aluno.id)
            
            with self._db_manager.get_cursor() as cursor:
                cursor.execute('''
                    UPDATE alunos 
                    SET nome = ?, idade = ?, curso = ?, nota = ?
                    WHERE id = ?
                ''', (*aluno.to_tuple(), aluno.id))
                
                return self.buscar_por_id(aluno.id)
        except AlunoNaoEncontradoError:
            raise
        except Exception as e:
            if isinstance(e, ErroBancoDados):
                raise
            raise ErroBancoDados("atualizar aluno", e)
    
    def remover(self, aluno_id: int) -> bool:
        """
        Remove um aluno do banco de dados
        
        Args:
            aluno_id: ID do aluno a ser removido
        
        Returns:
            True se removido com sucesso
        
        Raises:
            AlunoNaoEncontradoError: Se aluno não for encontrado
            ErroBancoDados: Se houver erro no banco
        """
        try:
            # Verificar se existe
            self.buscar_por_id(aluno_id)
            
            with self._db_manager.get_cursor() as cursor:
                cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
                return True
        except AlunoNaoEncontradoError:
            raise
        except Exception as e:
            if isinstance(e, ErroBancoDados):
                raise
            raise ErroBancoDados("remover aluno", e)
    
    def contar_total(self) -> int:
        """
        Retorna o total de alunos cadastrados
        
        Returns:
            Número total de alunos
        
        Raises:
            ErroBancoDados: Se houver erro no banco
        """
        try:
            with self._db_manager.get_cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM alunos")
                return cursor.fetchone()[0]
        except Exception as e:
            if isinstance(e, ErroBancoDados):
                raise
            raise ErroBancoDados("contar alunos", e)
    
    def obter_estatisticas(self) -> dict:
        """
        Obtém estatísticas do banco de dados
        
        Returns:
            Dicionário com estatísticas
        
        Raises:
            ErroBancoDados: Se houver erro no banco
        """
        try:
            stats = {}
            
            with self._db_manager.get_cursor() as cursor:
                # Total de alunos
                cursor.execute("SELECT COUNT(*) FROM alunos")
                stats['total'] = cursor.fetchone()[0]
                
                # Alunos por curso
                cursor.execute('''
                    SELECT curso, COUNT(*) as quantidade 
                    FROM alunos 
                    WHERE curso IS NOT NULL AND curso != ''
                    GROUP BY curso 
                    ORDER BY quantidade DESC
                ''')
                stats['por_curso'] = dict(cursor.fetchall())
                
                # Média das notas
                cursor.execute("SELECT AVG(nota) FROM alunos WHERE nota IS NOT NULL")
                resultado = cursor.fetchone()[0]
                stats['media_notas'] = round(resultado, 2) if resultado else None
                
                # Cadastrados hoje
                cursor.execute("SELECT COUNT(*) FROM alunos WHERE data_cadastro = DATE('now')")
                stats['cadastrados_hoje'] = cursor.fetchone()[0]
                
                # Melhor nota
                cursor.execute("SELECT MAX(nota), nome FROM alunos WHERE nota IS NOT NULL")
                resultado = cursor.fetchone()
                if resultado[0]:
                    stats['melhor_nota'] = {
                        'nota': round(resultado[0], 1),
                        'aluno': resultado[1]
                    }
                else:
                    stats['melhor_nota'] = None
            
            return stats
        except Exception as e:
            if isinstance(e, ErroBancoDados):
                raise
            raise ErroBancoDados("obter estatísticas", e)

