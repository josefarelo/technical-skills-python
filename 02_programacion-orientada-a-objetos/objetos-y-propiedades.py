class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")

# Crear instancia de Libro
mi_libro = Libro("1984", "George Orwell")
print("Libro inicial:")
mi_libro.mostrar_info()

# Modificar atributo
mi_libro.titulo = "Rebelión en la granja"
print("\nDespués de modificar:")
mi_libro.mostrar_info()

# Intentar acceder a atributo no existente (pero manejado)
try:
    print(mi_libro.paginas)
except AttributeError:
    print("\nError: El libro no tiene atributo 'paginas'")

# Añadir nuevo atributo dinámicamente
mi_libro.año_publicacion = 1945
print(f"\nAño de publicación añadido: {mi_libro.año_publicacion}")

# Mostrar todos los atributos actuales
print("\nAtributos actuales del libro:")
print(vars(mi_libro))