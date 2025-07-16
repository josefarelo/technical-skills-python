# Lista de frutas
frutas = ["manzana", "banana"]
print("Lista inicial de frutas:", frutas)

# Agregar una fruta a la lista
fruta_nueva = input("Ingresa una fruta para agregar a la lista: ")
frutas.append(fruta_nueva)
print("Lista de frutas actualizada:", frutas)

# Diccionario de persona
persona = {
    "nombre": "Ana",
    "edad": 25,
    "hobbies": ["leer", "correr"]
}
print("\nDatos iniciales de la persona:", persona)

# Agregar información al diccionario
ciudad = input("Ingresa la ciudad donde vive la persona: ")
persona["ciudad"] = ciudad

edad_actualizada = int(input("Ingresa la nueva edad de la persona: "))
persona["edad"] = edad_actualizada

print("Datos actualizados de la persona:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Set de números
numeros = {1, 2, 3, 2}  # El 2 duplicado no se agregará
print("\nSet inicial de números:", numeros)

# Operaciones con sets
numeros.add(5)
numeros.discard(1)  # Elimina el 1 si existe

otros_numeros = {4, 5, 6}
numeros.update(otros_numeros)  # Unión de sets

print("Set después de las operaciones:", numeros)
print("Números en común con {4, 5}:", numeros.intersection({4, 5}))

# lista de diccionarios
amigos = [
    {"nombre": "Carlos", "edad": 27},
    {"nombre": "Luisa", "edad": 23}
]
print("\nLista de amigos:", amigos)