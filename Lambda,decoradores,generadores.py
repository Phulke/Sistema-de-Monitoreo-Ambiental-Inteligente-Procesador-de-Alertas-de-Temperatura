import time
from functools import wraps  # Importamos functools

#Realizamos un decorador simple usando functools
def auditar_funcion(func):
    contador = 0
    @wraps(func)
    def inner(*args, **kwargs):
        nonlocal contador
        contador += 1
        print(f"Ejecutando '{func.__name__}' (llamada #{contador})...")
        inicio = time.time()
        resultado = func(*args, **kwargs)
        print(f"Duración: {time.time()-inicio:.4f}s\n")
        return resultado
    return inner

#Generador de datos
def leer_temperaturas():
    for t in [("CDMX", 26), ("Monterrey", 34), ("Toluca", 19),
              ("Cancún", 38), ("Guadalajara", 31), ("Puebla", 28)]:
        yield t

#Funcion para filtrar temperaturas
@auditar_funcion
def filtrar_temperaturas(datos):
    return list(filter(lambda t: t[1]>=30, datos))

#Funcion de alertas
@auditar_funcion
def transformar_alertas(datos):
    return list(map(lambda t: f"Alerta de calor en {t[0]}: {t[1]}°C", datos))

#Funcion para ordenar las temperaturas
@auditar_funcion
def ordenar_temperaturas(datos):
    return sorted(datos, key=lambda t: t[1], reverse=True)

#Funcion para realizar el promedio de temperaturas
@auditar_funcion
def calcular_promedio(datos):
    if not datos:
        return 0
    total = 0
    for t in datos:
        total += t[1]
    return total / len(datos)

#Funcion main
def main():
    datos = list(leer_temperaturas())
    filtrados = filtrar_temperaturas(datos)
    ordenados = ordenar_temperaturas(filtrados)
    alertas = transformar_alertas(ordenados)
    promedio = calcular_promedio(filtrados)

    print("ALERTAS DE TEMPERATURA EN:")
    for alerta in alertas:
        print(alerta)
    print(f"\nTemperatura promedio de alertas: {promedio:.1f}°C")

#Ejecutamos main
main()