# ===== Configuração do Banco de Dados =====
# Arquivo responsável pela criação e inicialização do banco de dados SQLite

import sqlite3

# ===== Função: Criar Banco de Dados =====
def criar_banco():
    # Estabelecer conexão com o arquivo banco.db (cria se não existir)
    conexao = sqlite3.connect('banco.db')
    # Criar cursor para executar comandos SQL
    cursor = conexao.cursor()

    # ===== Criar Tabela CHAMADO =====
    # Tabela que armazena informações dos chamados dos funcionários
    cursor.execute(''' 
                   CREATE TABLE IF NOT EXISTS CHAMADO (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   NOME_FUNCIONARIO TEXT,
                   SETOR_FUNCIONARIO TEXT,
                   PROBLEMA_DESCRITO TEXT,
                   STATUS_CHAMADO TEXT,
                   PRIORIADE_CHAMADO TEXT   
                   )
                   ''')
    # Confirmar (commit) as alterações no banco de dados
    conexao.commit()
    # Fechar a conexão com o banco de dados
    conexao.close()

# ===== Executar Inicialização =====
# Chamar a função para criar o banco de dados na primeira execução
criar_banco()
# Exibir mensagem de sucesso
print("Banco de dados criado com sucesso!🚀")
