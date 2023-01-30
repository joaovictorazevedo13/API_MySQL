from flask import Flask, make_response, jsonify, request
from bd import Carros
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="aplicacao",
    password="123456",
    database="api_mysql"
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False



@app.route("/carros", methods = ['GET'])
def get_carros():
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM api_mysql.carros')
    meus_carros = my_cursor.fetchall()
    
    carros = []    
    for carro in meus_carros:
        carros.append(
            {
            'id': carro[0],
            'marca': carro[1],
            'modelo': carro[2],
            'ano': carro[3]
            }
        )
    
    for dic in carros:
        for k, v in dic.items():
            print(f"{k}: {v}")
        print()
        
    return make_response(
        jsonify(
            mensagem = 'Lista de carros',
            dados = carros
        )
    )

@app.route("/carros", methods = ['POST'])
def post_carros():
    carro = request.json    
    my_cursor = mydb.cursor()    
    sql = f"INSERT INTO `api_mysql`.`carros` (`marca`, `modelo`, `ano`) VALUES ('{carro['marca']}', '{carro['modelo']}', {carro['ano']})"    
    my_cursor.execute(sql)
    mydb.commit()
        
    return make_response(
        jsonify(
            mensagem = 'Carro cadastrado com sucesso',
            carro = carro
        )
    )

if __name__ == "__main__":
    app.run(debug=True)
    
    
