import json
import requests
from typing import cast
import time
import math

""" URL1 = config('ULRICH', cast=str)
URL2 = config('YAEL', cast=str)
URL3 = config('DIEGO', cast=str)
valor = 0
i = 0
cpu = [(requests.post(URL1 + '/cpu').json().get("cpu"), URL1),
       (requests.post(URL2 + '/cpu').json().get("cpu"), URL2),
       (requests.post(URL3 + '/cpu').json().get("cpu"), URL3)] """

def obtener_rangos(nucleos, numeros_primos):
    a = numeros_primos/nucleos
    lista = [[0,0]]*nucleos
    j, i = 0, 1
    while j < nucleos:
        lista[j] = [int(math.floor(j*a)), int(math.ceil(i*a))]
        j += 1
        i += 1
    return lista


rangos = obtener_rangos(6, 500)
respuesta = []

for rango in rangos:
    response = requests.post('http://localhost:5000/calcular', json={"rango": rangos[0]})
    respuesta += response.json().get("arreglo")

print(respuesta)
print(len(respuesta))
