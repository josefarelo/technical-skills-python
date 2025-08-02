def verificar_edad(edad):
    # Verificar si la edad es mayor o igual a 18 porque es el límite legal para ser mayor de edad en la mayoría de países. Esto es importante para restringir acceso a contenido para adultos.
    return edad >= 18

def calcular_descuento(edad, es_socio):
    # Aplicar un descuento del 20% solo a mayores de edad que son socios porque la política de la empresa así lo establece para fidelizar clientes
    if verificar_edad(edad) and es_socio:
        return 0.2
    return 0.0

def main():
    # Datos de ejemplo para probar las funciones
    edad_usuario = 20
    es_socio_usuario = True
    
    # Mostrar el descuento aplicable al usuario
    # Esto ayuda en pruebas y demostraciones del sistema
    descuento = calcular_descuento(edad_usuario, es_socio_usuario)
    print(f"Descuento aplicable: {descuento * 100}%")

    # Comprobación adicional para registro de auditoría
    # Guardamos este registro por requisitos legales de protección de menores
    if verificar_edad(edad_usuario):
        print("Usuario verificado como mayor de edad")
    else:
        print("Acceso restringido a menores de edad")

if __name__ == "__main__":
    # Ejecutar la función principal solo si el script se ejecuta directamente
    # Esto permite usar las funciones como módulo sin ejecutar main() automáticamente
    main()