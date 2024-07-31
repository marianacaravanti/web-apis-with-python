from flask import Flask, jsonify, request

#Inicializa o app
app = Flask(__name__)

#Define o que o app faz
@app.get("/greet")
def index():
    """
        TODO:
        1. Capturar primeiro nome e sobrenome
        2. Se não for inserido, responda com um erro
        3. Se o primeiro nome não for inserido e o sobrenome for inserido:
           responda com "Olá, <sobrenome>!"
        4. Se o primeiro nome for inserido, mas o sobrenome não for inserido:
           responda com "Olá, <nome>!"
        5. Se ambos os nomes forem inseridos: responda com uma pergunta
           "O seu nome é <nome> <sobrenome>?"
    """
    response={"data": "Hello, World!"}
    return jsonify(response)

