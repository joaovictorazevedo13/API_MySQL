from flask import Flask, make_response, jsonify, request
from bd import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/carros", methods = ['GET'])
def get_carros():
    return make_response(
        jsonify(
            mensagem = 'Lista de carros',
            dados = Carros
        )
    )

@app.route("/carros", methods = ['POST'])
def post_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            mensagem = 'Carro cadastrado com sucesso',
            carro = carro
        )
    )

if __name__ == "__main__":
    app.run(debug=True)