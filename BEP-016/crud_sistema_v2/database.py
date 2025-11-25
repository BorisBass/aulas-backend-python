"""
Módulo de Gerenciamento de Banco de Dados
Aplica conceitos de BEP-017, BEP-018: Classes, Encapsulamento
"""

import sqlite3
from typing import Optional, Tuple
from contextlib import contextmanager

from .exceptions import ErroBancoDados


class DatabaseManager:
    """
    Classe para gerenciar conexões com banco de dados
    Aplica: Classes, Encapsulamento, Context Manager
    """
    
    def __init__(self, db_name: str = 'alunos_v2.db'):
        """
        Inicializa o gerenciador de banco de dados
        
        Args:
            db_name: Nome do arquivo do banco de dados
        """
        self._db_name = db_name
        self._connection: Optional[sqlite3.Connection] = None
        self._inicializado = False
    
    def conectar(self) -> sqlite3.Connection:
        """
        Conecta ao banco de dados e cria tabela se necessário
        
        Returns:
            Conexão SQLite
        
        Raises:
            ErroBancoDados: Se houver erro na conexão
        """
        try:
            if not self._connection:
                self._connection = sqlite3.connect(self._db_name)
                self._criar_tabela()
                print("✅ Banco de dados conectado e tabela criada!")
            return self._connection
        except sqlite3.Error as e:
            raise ErroBancoDados("conectar", e)
    
    def _criar_tabela(self):
        """Cria a tabela de alunos se não existir"""
        if not self._inicializado:
            cursor = self._connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER,
                    curso TEXT,
                    nota REAL,
                    data_cadastro DATE DEFAULT CURRENT_DATE
                )
            ''')
            self._connection.commit()
            self._inicializado = True
    
    @contextmanager
    def get_cursor(self):
        """
        Context manager para obter cursor do banco
        
        Yields:
            Cursor SQLite
        
        Raises:
            ErroBancoDados: Se houver erro
        """
        try:
            if not self._connection:
                self.conectar()
            cursor = self._connection.cursor()
            yield cursor
            self._connection.commit()
        except sqlite3.Error as e:
            if self._connection:
                self._connection.rollback()
            raise ErroBancoDados("executar operação", e)
        except Exception as e:
            if self._connection:
                self._connection.rollback()
            raise ErroBancoDados("executar operação", e)
    
    def fechar(self):
        """Fecha a conexão com o banco de dados"""
        if self._connection:
            try:
                self._connection.close()
                self._connection = None
                print("🔒 Conexão com banco fechada.")
            except sqlite3.Error as e:
                raise ErroBancoDados("fechar conexão", e)
    
    def __enter__(self):
        """Context manager: entrada"""
        self.conectar()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager: saída"""
        self.fechar()
        return False
    
    def __del__(self):
        """Destrutor: fecha conexão ao destruir objeto"""
        if self._connection:
            self.fechar()

