def operacion_asincrona(callback):
    print("Iniciando operación asíncrona... (esto podría ser una descarga o consulta a BD)")
    # Simulamos un retraso con time.sleep
    import time
    time.sleep(2)
    
    # Resultado ficticio de la operación
    resultado = {"status": "success", "data": [1, 2, 3], "code": 200}
    
    print("Operación completada, llamando al callback...")
    callback(resultado)

def mostrar_resultado(res):
    print("\n--- Callback ejecutado ---")
    print(f"Estado: {res['status']}")
    print(f"Datos recibidos: {res['data']}")
    print(f"Código de respuesta: {res['code']}")
    print("--------------------------")

def guardar_en_log(res):
    with open("log_operacion.txt", "a") as f:
        f.write(f"{res}\n")
    print("(Resultado guardado en log)")

# Probamos con el primer callback
operacion_asincrona(mostrar_resultado)

# Probamos con otro callback diferente
operacion_asincrona(guardar_en_log)