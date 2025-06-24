# Declaración de variables de tipos primitivos
edad = 30
precio = 19.99
nombre = "Juan Pérez"
es_estudiante = True

# Declaración de variables de tipos compuestos
materias = ["Matemáticas", "Historia", "Programación"]
calificaciones = {"Matemáticas": 85, "Historia": 92, "Programación": 88}

# Mostrar el tipo de cada variable
print("Tipos de variables primitivas:")
print(f"edad: {type(edad)}")
print(f"precio: {type(precio)}")
print(f"nombre: {type(nombre)}")
print(f"es_estudiante: {type(es_estudiante)}")

print("\nTipos de variables compuestas:")
print(f"materias: {type(materias)}")
print(f"calificaciones: {type(calificaciones)}")

# Operación adicional para mostrar uso práctico
print("\nInformación del estudiante:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Materias inscritas: {', '.join(materias)}")
print(f"Promedio: {sum(calificaciones.values())/len(calificaciones):.2f}")