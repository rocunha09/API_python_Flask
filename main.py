#importando libs
from flask import Flask, make_response, jsonify, request

#importanto dependencias do projeto
from db import Pacientes

#start do flask com o nome do projeto.
'''
--name__ = variável especial no Python que é usada para determinar
se o Python está executando o script como um programa principal ou
se está sendo importado como um módulo em outro script.
'''
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#rota get para raiz da aplicação.
'''
    o @ é um decorator que  usado para associar uma função Python a
    uma rota específica da sua aplicação web.
'''
#home
@app.route('/', methods=['GET'])
def home():
    return make_response (
            jsonify ('Home')
        )

#listar pacientes  
@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    return make_response (
            jsonify (
                    mensagem = "retorna lista de pacientes",
                    dados = Pacientes
                )
        )

#adicionar um paciente
@app.route('/pacientes', methods=['POST'])
def create_paciente():
    paciente = request.json
    Pacientes.append(paciente)
    return make_response (
            jsonify (
                    mensagem = "retorna o paciente criado",
                    dados = paciente
                )
        )
    



#rodando o servidor
app.run()