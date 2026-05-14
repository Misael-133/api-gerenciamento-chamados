# ===== API de Gerenciamento de Chamados =====

import sqlite3
from flask import Flask, request

# Inicializar a aplicação Flask.
# Flask é o framework que recebe as requisições e cuida das rotas.
app = Flask(__name__)

# Rota de teste para verificar se a API está funcionando.
@app.route('/api')
def api():
    return 'API rodando 🚀'


@app.route('/chamados', methods=['POST'])
def criar_chamado():

    # Pegar os dados que vieram no corpo da requisição em formato JSON.
    dados = request.get_json()

    # Cada variável recebe uma informação do JSON enviado.
    nome_funcionario = dados.get('nome_funcionario')
    setor_funcionario = dados.get('setor_funcionario')
    problema_descrito = dados.get('problema_descrito')

    # Abrir conexão com o banco SQLite local.
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    # Inserir os dados do chamado na tabela 'chamados'.
    cursor.execute('''
    INSERT INTO chamados (
        nome_funcionario,
        setor_funcionario,
        problema_descrito
    )
    VALUES (?, ?, ?)
    ''', (
        nome_funcionario,
        setor_funcionario,
        problema_descrito
    ))

    # Salvar as alterações no banco.
    conexao.commit()

    # Fechar a conexão para liberar recursos.
    conexao.close()

    # Retornar uma mensagem dizendo que deu certo.
    return {
        "mensagem": "Chamado criado com sucesso!",
        "funcionario": nome_funcionario
    }

# Rota para listar todos os chamados salvos no banco.
@app.route('/chamados', methods=['GET'])
def listar_chamados():
    # Abrir conexão com o banco SQLite.
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    # Buscar todos os registros da tabela 'chamados'.
    cursor.execute('SELECT * FROM chamados')
    chamados = cursor.fetchall()

    # Criar uma lista de chamados em formato de dicionários para retornar.
    lista_chamados = []
    for linha in chamados:
        id_chamado, nome_funcionario, setor_funcionario, problema_descrito = linha
        chamado = {
            "id": id_chamado,
            "nome_funcionario": nome_funcionario,
            "setor_funcionario": setor_funcionario,
            "problema_descrito": problema_descrito,
            "status": "status",
            "prioridade": "prioridade"
        }
        lista_chamados.append(chamado)

    # Fechar a conexão com o banco.
    conexao.close()

    # Retornar a lista de chamados para quem pediu.
    return {
        "chamados": lista_chamados
    }



if __name__ == '__main__':
    app.run(debug=True)