# ===== API de Gerenciamento de Chamados =====

import sqlite3
from flask import Flask, request

# Inicializar a aplicação Flask.
# Flask é o framework responsável pelas rotas e requisições HTTP.
app = Flask(__name__)

# =========================================================
# ROTA TESTE
# =========================================================

@app.route('/api')
def api():
    return 'API rodando 🚀'


# =========================================================
# CRIAR CHAMADO (POST)
# =========================================================

@app.route('/chamados', methods=['POST'])
def criar_chamado():

    # Pegar os dados enviados em JSON.
    dados = request.get_json()

    # Extrair cada informação do JSON.
    nome_funcionario = dados.get('nome_funcionario')
    setor_funcionario = dados.get('setor_funcionario')
    problema_descrito = dados.get('problema_descrito')
    status = dados.get('status')
    prioridade = dados.get('prioridade')

    # Abrir conexão com o banco.
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    # Inserir dados na tabela.
    cursor.execute('''
    INSERT INTO chamados (
        nome_funcionario,
        setor_funcionario,
        problema_descrito,
        status,
        prioridade
    )
    VALUES (?, ?, ?, ?, ?)
    ''', (
        nome_funcionario,
        setor_funcionario,
        problema_descrito,
        status,
        prioridade
    ))

    # Salvar alterações.
    conexao.commit()

    # Fechar conexão.
    conexao.close()

    # Retorno da API.
    return {
        "mensagem": "Chamado criado com sucesso!",
        "funcionario": nome_funcionario
    }


# =========================================================
# LISTAR CHAMADOS (GET)
# =========================================================

@app.route('/chamados', methods=['GET'])
def listar_chamados():

    # Abrir conexão com banco.
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    # Buscar todos os chamados.
    cursor.execute('SELECT * FROM chamados')

    # fetchall() pega todos os registros encontrados.
    chamados = cursor.fetchall()

    # Lista final que será retornada em JSON.
    lista_chamados = []

    # Percorrer cada linha retornada do banco.
    for linha in chamados:

        # Cada variável recebe uma coluna da tabela.
        id_chamado, nome_funcionario, setor_funcionario, problema_descrito, status, prioridade = linha

        # Transformar os dados em dicionário.
        chamado = {
            "id": id_chamado,
            "nome_funcionario": nome_funcionario,
            "setor_funcionario": setor_funcionario,
            "problema_descrito": problema_descrito,
            "status": status,
            "prioridade": prioridade
        }

        # Adicionar chamado na lista.
        lista_chamados.append(chamado)

    # Fechar conexão.
    conexao.close()

    # Retornar JSON final.
    return {
        "chamados": lista_chamados
    }


# =========================================================
# INICIAR SERVIDOR FLASK
# =========================================================

if __name__ == '__main__':
    app.run(debug=True)