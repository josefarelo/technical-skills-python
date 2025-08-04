def obtener_nombre():
    """Solicita y retorna el nombre del usuario."""
    nombre = input("Por favor, ingresa tu nombre: ")
    return nombre

def crear_mensaje(nombre):
    """Genera un mensaje de bienvenida personalizado."""
    return f"Hola {nombre}, ¡bienvenido/a al programa!"

def mostrar_mensaje(mensaje):
    """Muestra un mensaje en pantalla."""
    print(mensaje)

def main():
    """Función principal que coordina el flujo del programa."""
    nombre_usuario = obtener_nombre()
    mensaje_bienvenida = crear_mensaje(nombre_usuario)
    mostrar_mensaje(mensaje_bienvenida)

if __name__ == "__main__":
    main()