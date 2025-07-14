def lens_get(key, dictionary):
    """Obtiene el valor de una clave en un diccionario de forma segura."""
    if not isinstance(dictionary, dict):
        raise ValueError("El segundo argumento debe ser un diccionario")
    return dictionary.get(key, None)

def lens_set(key, value, dictionary):
    """Crea una copia del diccionario y actualiza el valor de la clave especificada."""
    if not isinstance(dictionary, dict):
        raise ValueError("El tercer argumento debe ser un diccionario")
    
    new_dict = dictionary.copy()
    new_dict[key] = value
    return new_dict

def lens_update(keys, value, dictionary):
    """Actualiza un valor anidado en el diccionario de forma inmutable."""
    if not keys or not isinstance(keys, list):
        raise ValueError("Las claves deben ser una lista no vacía")
    
    new_dict = dictionary.copy()
    current = new_dict
    
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    
    current[keys[-1]] = value
    return new_dict

# Ejemplo
persona = {"nombre": "Ana", "edad": 25, "direccion": {"ciudad": "Madrid"}}

# Obtener valores
edad = lens_get("edad", persona)
ciudad = lens_get("ciudad", lens_get("direccion", persona))

# Modificar valores
persona_actualizada = lens_set("edad", 26, persona)
persona_con_telefono = lens_set("telefono", "123456789", persona_actualizada)

# Modificar valores anidados
persona_direccion_actualizada = lens_update(["direccion", "ciudad"], "Barcelona", persona)

print("Persona original:", persona)
print("Edad obtenida:", edad)
print("Ciudad obtenida:", ciudad)
print("Persona con edad actualizada:", persona_actualizada)
print("Persona con teléfono añadido:", persona_con_telefono)
print("Persona con dirección actualizada:", persona_direccion_actualizada)