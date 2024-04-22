# API - É um lugar para disponibilizar recursos e/ou funcionalidades.

# 1. Objetivo - Criar uma API que dispibiliza a consulta, criação, edição e exclusão de produtos.

# 2. URL Base - localhost - exemplo: localhost:5000/produtos/....

# 3. EndPoints:
#   - localhost/produtos (GET)
#   - localhost/produtos/{id} (GET)
#   - localhost/produtos/create (POST)
#   - localhost/produtos/edit/{id} (PUT)
#   - localhost/produtos/delete/{id} (DELETE)

# 4. Quais recursos queremos disponibilizar - Produtos variados

from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

import jwt
from jwt import InvalidSignatureError

import datetime

app = Flask(__name__)

payload = {
    "sub": "matheus"
}

senha = 'senha-secreta'

token = jwt.encode(
    payload=payload,
    key=senha
)

print('Token:', token)

produtos = [
    {
        'id': 1,
        'nome': 'Senhor dos Anéis - A Sociedade do Anel',
        'preco': 'R$ 200,00',
        'tipo': 'Livro',
        'data': '10/04/2024',
        'dataCompra': '15/04/2024'
    },
    {
        'id': 2,
        'nome': 'A História sem Fim',
        'preco': 'R$ 150,00',
        'tipo': 'Livro',
        'data': '10/04/2024',
        'dataCompra': '15/04/2024'
    },
    {
        'id': 3,
        'nome': 'Caneta Bic',
        'preco': 'R$ 7,00',
        'tipo': 'Material Escolar',
        'data': '10/04/2024',
        'dataCompra': '17/04/2024'
    },
    {
        'id': 4,
        'nome': 'Relógio de Parede',
        'preco': 'R$ 25,00',
        'tipo': 'Decoração',
        'data': '10/04/2024',
        'dataCompra': '14/04/2024'
    },
    {
        'id': 5,
        'nome': 'Delineador',
        'preco': 'R$ 40,00',
        'tipo': 'Maquiagem',
        'data': '10/04/2024',
        'dataCompra': '13/04/2024'
    },
    {
        'id': 6,
        'nome': 'Teclado',
        'preco': 'R$ 100,00',
        'tipo': 'Periféricos',
        'data': '10/04/2024',
        'dataCompra': '20/04/2024'
    },
    {
        'id': 7,
        'nome': 'Mouse',
        'preco': 'R$ 70,00',
        'tipo': 'Preiféricos',
        'data': '10/04/2024',
        'dataCompra': '20/04/2024'
    },
    {
        'id': 8,
        'nome': 'Headset',
        'preco': 'R$ 150,00',
        'tipo': 'Preiféricos',
        'data': '10/04/2024',
        'dataCompra': '20/04/2024'
    },
    {
        'id': 9,
        'nome': 'Brincos',
        'preco': 'R$ 10,00',
        'tipo': 'Bijuteria',
        'data': '10/04/2024',
        'dataCompra': '11/04/2024'
    },
    {
        'id': 10,
        'nome': 'Colar',
        'preco': 'R$ 15,00',
        'tipo': 'Bijuteria',
        'data': '10/04/2024',
        'dataCompra': '11/04/2024'
    },
]

print(jwt.decode(token, key=senha, algorithms=['HS256', ]))

fake_token = token

# Teste de Token invalidado (Tirar o comentário para o teste)
#fake_token = token.replace('X4','X0')

print(fake_token)


try:
    print ('Token validado com sucesso! Continuando o processo.')
    print(jwt.decode(fake_token, key=senha, algorithms=['HS256', ]))
    valid = 'validado'
except InvalidSignatureError as e:
    print('Token não foi validado', '\n', e)
    valid = 'error'

if valid == 'error':
    print ('Finalizando API devido a falha na segurança.')
    exit()
    
# Criar uma API que permite:
# Consultar (TODOS)


@app.route('/produtos', methods=['GET'])
def obter_produtos():
    return jsonify(produtos)

# Consultar (ID)


@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produtos_selecionados(id):
    for produto in produtos:
        if produto.get('id') == id:
            return jsonify(produto)

# Editar


@app.route('/produtos/edit/<int:id>', methods=['PUT'])
def editar_produtos_selecionados(id):
    produto_alterado = request.get_json()
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            produtos[indice].update(produto_alterado)
            return jsonify(produtos[indice])

# Criar


@app.route('/produtos/create', methods=['POST'])
def criar_produtos():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    return jsonify(produtos)

# Excluir


@app.route('/produtos/delete/<int:id>', methods=['DELETE'])
def excluir_produtos(id):
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            del produtos[indice]

    return jsonify(produtos)


app.run(port=5000, host='localhost', debug=True)
