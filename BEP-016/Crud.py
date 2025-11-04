import sqlite3
import os

def conectar_banco():
    """Conecta ao banco de dados"""
    try:
        conn = sqlite3.connect('alunos.db')
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

def exibir_menu():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("🎓 SISTEMA DE GERENCIAMENTO DE ALUNOS")
    print("="*50)
    print("1. 📝 Cadastrar novo aluno")
    print("2. 📋 Listar todos os alunos")
    print("3. 🔍 Buscar aluno por nome")
    print("4. ✏️ Atualizar dados do aluno")
    print("5. 🗑️ Remover aluno")
    print("6. 📊 Estatísticas")
    print("0. 🚪 Sair")
    print("="*50)

def cadastrar_aluno(cursor, conn):
    """Cadastra um novo aluno"""
    try:
        print("\n📝 CADASTRO DE NOVO ALUNO")
        print("-" * 30)
        
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

def listar_alunos(cursor):
    """Lista todos os alunos"""
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
            id_aluno, nome, idade, curso, nota, data = aluno
            idade_display = idade if idade else "N/A"
            curso_display = curso if curso else "N/A"
            nota_display = f"{nota:.1f}" if nota else "N/A"
            print(f"{id_aluno:<3} {nome:<25} {idade_display:<5} {curso_display:<15} {nota_display:<5} {data}")
            
    except sqlite3.Error as e:
        print(f"❌ Erro ao listar alunos: {e}")


def buscar_aluno(cursor):
    """Busca aluno por nome"""
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
            id_aluno, nome, idade, curso, nota, data = aluno
            idade_display = idade if idade else "N/A"
            curso_display = curso if curso else "N/A"
            nota_display = f"{nota:.1f}" if nota else "N/A"
            print(f"{id_aluno:<3} {nome:<25} {idade_display:<5} {curso_display:<15} {nota_display:<5} {data}")
            
    except sqlite3.Error as e:
        print(f"❌ Erro ao buscar aluno: {e}")     

def atualizar_aluno(cursor, conn):
    """Atualiza dados de um aluno"""
    try:
        print("\n✏️ ATUALIZAR DADOS DO ALUNO")
        print("-" * 30)
        
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

def remover_aluno(cursor, conn):
    """Remove um aluno"""
    try:
        print("\n🗑️ REMOVER ALUNO")
        print("-" * 30)
        
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

def mostrar_estatisticas(cursor):
    """Mostra estatísticas do banco"""
    try:
        print("\n📊 ESTATÍSTICAS DO SISTEMA")
        print("-" * 30)
        
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

def main():
    """Função principal do programa"""
    print("🚀 Iniciando Sistema de Gerenciamento de Alunos...")
    
    # Conectar ao banco
    conn, cursor = conectar_banco()
    if not conn:
        print("❌ Não foi possível conectar ao banco. Encerrando...")
        return
    
    try:
        while True:
            exibir_menu()
            opcao = input("👉 Escolha uma opção: ").strip()
            
            if opcao == '1':
                cadastrar_aluno(cursor, conn)
            elif opcao == '2':
                listar_alunos(cursor)
            elif opcao == '3':
                buscar_aluno(cursor)
            elif opcao == '4':
                atualizar_aluno(cursor, conn)
            elif opcao == '5':
                remover_aluno(cursor, conn)
            elif opcao == '6':
                mostrar_estatisticas(cursor)
            elif opcao == '0':
                print("\n👋 Obrigado por usar o sistema! Até logo!")
                break
            else:
                print("❌ Opção inválida! Tente novamente.")
            
            input("\n⏸️ Pressione Enter para continuar...")
    
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
    finally:
        # Sempre fechar a conexão
        if conn:
            conn.close()
            print("🔒 Conexão com banco fechada.")

# Executar o programa
if __name__ == "__main__":
    main()        
