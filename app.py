from flask import Flask, jsonify, request
import primo
import psutil

rango = [0]*2
arreglo = []

app = Flask(__name__)

@app.route('/calcular', methods=['POST'])
def suma():
    rango = list(request.json.get("rango"))
    return jsonify({
                "arreglo": list(primo.calcular_primos(rango[0], rango[1])),
                "rango": str(rango)
            })

@app.route('/cpu', methods=['POST'])
def obtener_cpu():
    return jsonify({"cpu": psutil.cpu_count()})

if __name__ == '__main__':
    app.run(host='localhost', debug=True) 
