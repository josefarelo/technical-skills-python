mensaje = "Global"

def cambiar_mensaje():
    mensaje = "Local"
    print("Dentro de la función:", mensaje)

print("Antes de llamar a la función:", mensaje)
cambiar_mensaje()
print("Después de llamar a la función:", mensaje)

def otra_funcion():
    global mensaje
    mensaje = "Cambiado con global"
    print("Dentro de otra_funcion:", mensaje)

print("\n--- Probando con global ---")
print("Antes de otra_funcion:", mensaje)
otra_funcion()
print("Después de otra_funcion:", mensaje)

def funcion_con_error():
    try:
        print("Intentando acceder a variable_local:", variable_local)
    except NameError as e:
        print(f"Error: {e}")

print("\n--- Probando acceso a variables locales ---")
variable_local = "Soy local"
funcion_con_error()

def funcion_anidada():
    mensaje_externo = "Externo"
    
    def interna():
        nonlocal mensaje_externo
        mensaje_externo = "Modificado desde interna"
        print("Dentro de interna:", mensaje_externo)
    
    print("Antes de llamar a interna:", mensaje_externo)
    interna()
    print("Después de llamar a interna:", mensaje_externo)

print("\n--- Probando nonlocal ---")
funcion_anidada()