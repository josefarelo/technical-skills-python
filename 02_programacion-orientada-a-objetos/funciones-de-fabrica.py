def crear_usuario(nombre, edad, email=None, activo=True):
    usuario = {
        "nombre": nombre,
        "edad": edad,
        "activo": activo
    }
    
    if email is not None:
        usuario["email"] = email
    
    return usuario

# Ejemplos de uso
usuario1 = crear_usuario("Ana", 25)
usuario2 = crear_usuario("Luis", 30, "luis@example.com", False)
usuario3 = crear_usuario("Carlos", 40, activo=True)

print("Usuario 1:", usuario1)
print("Usuario 2:", usuario2)
print("Usuario 3:", usuario3)

# Modificar un usuario después de creado
usuario1["edad"] = 26
print("Usuario 1 actualizado:", usuario1)