"""
Módulo de Gerenciamento de Banco de Dados
Aplica conceitos básicos de BEP-017: Classes simples
"""

import sqlite3


class DatabaseManager:
    """
    Classe para gerenciar conexões com banco de dados
    Versão simplificada - sem context managers avançados
    """
    
    def __init__(self, db_name='tarefas.db'):
        """
        Inicializa o gerenciador de banco de dados
        
        Args:
            db_name: Nome do arquivo do banco de dados
        """
        self.db_name = db_name
        self.connection = None
    
    def conectar(self):
        """
        Conecta ao banco de dados e cria tabela se necessário
        
        Returns:
            Conexão SQLite
        """
        try:
            if not self.connection:
                self.connection = sqlite3.connect(self.db_name)
                self._criar_tabela()
                print("✅ Banco de dados conectado e tabela criada!")
            return self.connection
        except sqlite3.Error as e:
            print(f"❌ Erro ao conectar: {e}")
            return None
    
    def _criar_tabela(self):
        """Cria a tabela de tarefas se não existir"""
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                concluida INTEGER DEFAULT 0,
                data_criacao DATE DEFAULT CURRENT_DATE
            )
        ''')
        self.connection.commit()
    
    def get_cursor(self):
        """
        Retorna um cursor do banco de dados
        
        Returns:
            Cursor SQLite
        """
        if not self.connection:
            self.conectar()
        return self.connection.cursor()
    
    def fechar(self):
        """Fecha a conexão com o banco de dados"""
        if self.connection:
            try:
                self.connection.close()
                self.connection = None
                print("🔒 Conexão com banco fechada.")
            except sqlite3.Error as e:
                print(f"❌ Erro ao fechar conexão: {e}")




