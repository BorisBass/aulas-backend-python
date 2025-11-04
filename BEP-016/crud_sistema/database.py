"""
Módulo de Conexão com Banco de Dados
Responsável por: conexão, criação de tabelas e gerenciamento de conexões
"""

import sqlite3
import os
from typing import Optional, Tuple


# Configuração do banco de dados
DB_NAME = 'alunos.db'


def conectar_banco() -> Tuple[Optional[sqlite3.Connection], Optional[sqlite3.Cursor]]:
    """
    Conecta ao banco de dados SQLite e cria a tabela se não existir.
    
    Returns:
        Tuple[Connection, Cursor]: Tupla com conexão e cursor, ou (None, None) em caso de erro
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Criar tabela se não existir
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
        conn.commit()
        print("✅ Banco de dados conectado e tabela criada!")
        return conn, cursor
    except sqlite3.Error as e:
        print(f"❌ Erro ao conectar: {e}")
        return None, None


def fechar_conexao(conn: sqlite3.Connection) -> None:
    """
    Fecha a conexão com o banco de dados.
    
    Args:
        conn: Conexão SQLite a ser fechada
    """
    if conn:
        try:
            conn.close()
            print("🔒 Conexão com banco fechada.")
        except sqlite3.Error as e:
            print(f"❌ Erro ao fechar conexão: {e}")

