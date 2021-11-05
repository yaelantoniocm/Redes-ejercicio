from flask import Flask, jsonify, request
from utils import suma_peticion
from getmac import get_mac_address as gma
import psutil

app = Flask(__name__)

@app.route('/', methods=['GET'])
def recibe():
    return jsonify({"valor": 0})

@app.route('/suma', methods=['POST'])
def suma():
    return jsonify({
                    "valor": suma_peticion(request),
                    "mac": str(gma()),
                    "name": "Yael"
                   })

@app.route('/ram', methods=['POST'])
def obtener_ram():
    return jsonify({"ram": psutil.virtual_memory().total})

@app.route('/finalizado', methods=['POST'])
def finalizar():
    name = request.json.get("name")
    print(str("Algoritmo finalizado por " + name))
    return str("Algoritmo finalizado por " + name)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)