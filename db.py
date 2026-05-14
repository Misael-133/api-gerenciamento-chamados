import sqlite3

def criar_banco():

    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chamados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_funcionario TEXT,
        setor_funcionario TEXT,
        problema_descrito TEXT,
        status TEXT,
        prioridade TEXT
    )
    ''')

    conexao.commit()
    conexao.close()

    print("Banco de dados criado com sucesso! 🚀")

criar_banco()