def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit.
    
    Args:
        celsius (float): Temperatura en grados Celsius.
        
    Returns:
        float: Temperatura convertida a Fahrenheit.
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("La temperatura debe ser un número")
        
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)

# Pruebas básicas
print("Pruebas de conversión Celsius a Fahrenheit:")
print(f"0°C -> {celsius_a_fahrenheit(0)}°F")        #    32°F
print(f"100°C -> {celsius_a_fahrenheit(100)}°F")    #    212°F
print(f"37.5°C -> {celsius_a_fahrenheit(37.5)}°F")  #    99.5°F

# Prueba con entrada inválida
try:
    print(f"'hola'°C -> {celsius_a_fahrenheit('hola')}°F")
except TypeError as e:
    print(f"Error esperado: {e}")