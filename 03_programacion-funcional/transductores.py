def mapear(func_transformacion):
    def aplicar(iterable):
        return map(func_transformacion, iterable)
    return aplicar

def filtrar(func_condicion):
    def aplicar(iterable):
        return filter(func_condicion, iterable)
    return aplicar

def transduce(transformaciones, iterable):
    datos_transformados = iterable
    for transformacion in transformaciones:
        datos_transformados = transformacion(datos_transformados)
    return list(datos_transformados)

if __name__ == "__main__":
    numeros = [10, 20, 30, 40, 50, 60]
    
    duplicar = mapear(lambda x: x * 2)
    mayores_a_50 = filtrar(lambda x: x > 50)
    
    pipeline = [duplicar, mayores_a_50]
    
    resultado_final = transduce(pipeline, numeros)
    print("Resultado:", resultado_final)  # [120]
    
    # Ejemplo adicional
    otros_datos = [1, 2, 3, 4, 5]
    otro_resultado = transduce(
        [
            mapear(lambda n: n * 3),
            filtrar(lambda n: n % 2 == 0),
            mapear(lambda n: n - 1)
        ],
        otros_datos
    )
    print("Otro resultado:", otro_resultado)  # [5, 11]