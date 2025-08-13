def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Inicio de ejecución de {func.__name__}")
        print(f"[LOG] Argumentos posicionales: {args}")
        print(f"[LOG] Argumentos clave: {kwargs}")
        
        resultado = func(*args, **kwargs)
        
        print(f"[LOG] Fin de ejecución de {func.__name__}")
        print(f"[LOG] Retorno: {resultado}")
        return resultado
    return wrapper

@logger
def sumar(a, b):
    """Suma dos números"""
    return a + b

@logger
def saludar(nombre, saludo="Hola"):
    """Saluda a una persona"""
    print(f"{saludo}, {nombre}!")
    return f"{saludo.lower()}_{nombre}"

if __name__ == "__main__":
    print("-- Probando función sumar --")
    resultado_suma = sumar(5, 3)
    print(f"Resultado suma: {resultado_suma}\n")
    
    print("-- Probando función saludar --")
    resultado_saludo = saludar("Juan", saludo="Buenos días")
    print(f"Resultado saludo: {resultado_saludo}\n")
    
    print("-- Probando con argumentos por defecto --")
    resultado_saludo2 = saludar("Ana")
    print(f"Resultado saludo2: {resultado_saludo2}")