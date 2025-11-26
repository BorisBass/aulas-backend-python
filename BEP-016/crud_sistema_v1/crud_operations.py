"""
Módulo de Operações CRUD
Responsável por: Create, Read, Update, Delete e Estatísticas
"""

import sqlite3
from typing import Optional
from .menu import exibir_cabecalho, formatar_aluno


def cadastrar_aluno(cursor: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    """Cadastra um novo aluno no banco de dados"""
    try:
        exibir_cabecalho("📝 CADASTRO DE NOVO ALUNO")
        
        nome = input("Nome completo: ").strip()
        if not nome:
            print("❌ Nome é obrigatório!")
            return
        
        idade = input("Idade: ").strip()
        if idade:
            try:
                idade = int(idade)
            except ValueError:
                print("❌ Idade deve ser um número!")
                return
        
        curso = input("Curso: ").strip()
        
        nota = input("Nota (0-10): ").strip()
        if nota:
            try:
                nota = float(nota)
                if nota < 0 or nota > 10:
                    print("❌ Nota deve estar entre 0 e 10!")
                    return
            except ValueError:
                print("❌ Nota deve ser um número!")
                return
        
        # Inserir no banco
        cursor.execute('''
            INSERT INTO alunos (nome, idade, curso, nota)
            VALUES (?, ?, ?, ?)
        ''', (nome, idade, curso, nota))
        
        conn.commit()
        print(f"✅ Aluno '{nome}' cadastrado com sucesso!")
        
    except sqlite3.Error as e:
        print(f"❌ Erro no banco: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


def listar_alunos(cursor: sqlite3.Cursor) -> None:
    """Lista todos os alunos cadastrados"""
    try:
        cursor.execute("SELECT * FROM alunos ORDER BY nome")
        alunos = cursor.fetchall()
        
        if not alunos:
            print("📭 Nenhum aluno cadastrado!")
            return
        
        print(f"\n📋 LISTA DE ALUNOS ({len(alunos)} cadastrados)")
        print("-" * 90)
        print(f"{'ID':<3} {'Nome':<25} {'Idade':<5} {'Curso':<15} {'Nota':<5} {'Data'}")
        print("-" * 90)
        
        for aluno in alunos:
            print(formatar_aluno(aluno))
            
    except sqlite3.Error as e:
        print(f"❌ Erro ao listar alunos: {e}")


def buscar_aluno(cursor: sqlite3.Cursor) -> None:
    """Busca alunos por nome usando LIKE"""
    try:
        nome_busca = input("\n🔍 Digite o nome para buscar: ").strip()
        if not nome_busca:
            print("❌ Digite um nome para buscar!")
            return
        
        cursor.execute("SELECT * FROM alunos WHERE nome LIKE ? ORDER BY nome", 
                      (f"%{nome_busca}%",))
        alunos = cursor.fetchall()
        
        if not alunos:
            print(f"📭 Nenhum aluno encontrado com '{nome_busca}'")
            return
        
        print(f"\n🔍 RESULTADO DA BUSCA por '{nome_busca}' ({len(alunos)} encontrados)")
        print("-" * 90)
        print(f"{'ID':<3} {'Nome':<25} {'Idade':<5} {'Curso':<15} {'Nota':<5} {'Data'}")
        print("-" * 90)
        
        for aluno in alunos:
            print(formatar_aluno(aluno))
            
    except sqlite3.Error as e:
        print(f"❌ Erro ao buscar aluno: {e}")


def atualizar_aluno(cursor: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    """Atualiza dados de um aluno existente"""
    try:
        exibir_cabecalho("✏️ ATUALIZAR DADOS DO ALUNO")
        
        # Mostrar lista para facilitar escolha
        cursor.execute("SELECT id, nome FROM alunos ORDER BY nome")
        alunos = cursor.fetchall()
        
        if not alunos:
            print("📭 Nenhum aluno cadastrado!")
            return
        
        print("📋 Alunos disponíveis:")
        for aluno in alunos:
            print(f"  {aluno[0]} - {aluno[1]}")
        
        aluno_id = input("\nDigite o ID do aluno: ").strip()
        if not aluno_id:
            print("❌ ID é obrigatório!")
            return
        
        try:
            aluno_id = int(aluno_id)
        except ValueError:
            print("❌ ID deve ser um número!")
            return
        
        # Verificar se aluno existe
        cursor.execute("SELECT nome FROM alunos WHERE id = ?", (aluno_id,))
        aluno_existe = cursor.fetchone()
        
        if not aluno_existe:
            print("❌ Aluno não encontrado!")
            return
        
        print(f"\n📝 Atualizando dados de: {aluno_existe[0]}")
        print("Deixe em branco para manter o valor atual")
        
        nome = input("Nome: ").strip()
        idade = input("Idade: ").strip()
        curso = input("Curso: ").strip()
        nota = input("Nota: ").strip()
        
        # Construir query de atualização
        campos_atualizar = []
        valores = []
        
        if nome:
            campos_atualizar.append("nome = ?")
            valores.append(nome)
        
        if idade:
            try:
                idade = int(idade)
                campos_atualizar.append("idade = ?")
                valores.append(idade)
            except ValueError:
                print("❌ Idade deve ser um número!")
                return
        
        if curso:
            campos_atualizar.append("curso = ?")
            valores.append(curso)
        
        if nota:
            try:
                nota = float(nota)
                if nota < 0 or nota > 10:
                    print("❌ Nota deve estar entre 0 e 10!")
                    return
                campos_atualizar.append("nota = ?")
                valores.append(nota)
            except ValueError:
                print("❌ Nota deve ser um número!")
                return
        
        if not campos_atualizar:
            print("❌ Nenhum campo foi alterado!")
            return
        
        valores.append(aluno_id)
        query = f"UPDATE alunos SET {', '.join(campos_atualizar)} WHERE id = ?"
        
        cursor.execute(query, valores)
        conn.commit()
        print(f"✅ Aluno {aluno_id} atualizado com sucesso!")
        
    except sqlite3.Error as e:
        print(f"❌ Erro no banco: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


def remover_aluno(cursor: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    """Remove um aluno do banco de dados"""
    try:
        exibir_cabecalho("🗑️ REMOVER ALUNO")
        
        # Mostrar lista para facilitar escolha
        cursor.execute("SELECT id, nome FROM alunos ORDER BY nome")
        alunos = cursor.fetchall()
        
        if not alunos:
            print("📭 Nenhum aluno cadastrado!")
            return
        
        print("📋 Alunos disponíveis:")
        for aluno in alunos:
            print(f"  {aluno[0]} - {aluno[1]}")
        
        aluno_id = input("\nDigite o ID do aluno para remover: ").strip()
        if not aluno_id:
            print("❌ ID é obrigatório!")
            return
        
        try:
            aluno_id = int(aluno_id)
        except ValueError:
            print("❌ ID deve ser um número!")
            return
        
        # Verificar se aluno existe
        cursor.execute("SELECT nome FROM alunos WHERE id = ?", (aluno_id,))
        aluno_existe = cursor.fetchone()
        
        if not aluno_existe:
            print("❌ Aluno não encontrado!")
            return
        
        # Confirmação
        confirmacao = input(f"\n⚠️ Tem certeza que deseja remover '{aluno_existe[0]}'? (s/n): ").strip().lower()
        
        if confirmacao == 's':
            cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
            conn.commit()
            print(f"✅ Aluno '{aluno_existe[0]}' removido com sucesso!")
        else:
            print("❌ Operação cancelada.")
        
    except sqlite3.Error as e:
        print(f"❌ Erro no banco: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


def mostrar_estatisticas(cursor: sqlite3.Cursor) -> None:
    """Mostra estatísticas do banco de dados"""
    try:
        exibir_cabecalho("📊 ESTATÍSTICAS DO SISTEMA")
        
        # Total de alunos
        cursor.execute("SELECT COUNT(*) FROM alunos")
        total = cursor.fetchone()[0]
        print(f"👥 Total de alunos: {total}")
        
        if total == 0:
            print("📭 Nenhum aluno cadastrado para estatísticas!")
            return
        
        # Alunos por curso
        cursor.execute('''
            SELECT curso, COUNT(*) as quantidade 
            FROM alunos 
            WHERE curso IS NOT NULL AND curso != ''
            GROUP BY curso 
            ORDER BY quantidade DESC
        ''')
        cursos = cursor.fetchall()
        
        if cursos:
            print(f"\n📚 Alunos por curso:")
            for curso, qtd in cursos:
                print(f"  {curso}: {qtd} aluno(s)")
        
        # Média das notas
        cursor.execute("SELECT AVG(nota) FROM alunos WHERE nota IS NOT NULL")
        media = cursor.fetchone()[0]
        if media:
            print(f"\n📈 Média das notas: {media:.2f}")
        
        # Alunos cadastrados hoje
        cursor.execute("SELECT COUNT(*) FROM alunos WHERE data_cadastro = DATE('now')")
        hoje = cursor.fetchone()[0]
        print(f"\n📅 Cadastrados hoje: {hoje}")
        
        # Melhor nota
        cursor.execute("SELECT MAX(nota), nome FROM alunos WHERE nota IS NOT NULL")
        melhor = cursor.fetchone()
        if melhor[0]:
            print(f"\n🏆 Melhor nota: {melhor[0]:.1f} - {melhor[1]}")
        
    except sqlite3.Error as e:
        print(f"❌ Erro ao gerar estatísticas: {e}")

