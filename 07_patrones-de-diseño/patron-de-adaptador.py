class Printer:
    def print_lower(self, msg):
        print(msg.lower())

class Adapter:
    def __init__(self, printer):
        self.printer = printer
    
    def print_upper(self, msg):
        # Convertimos el mensaje a mayúsculas antes de pasarlo al Printer
        upper_msg = msg.upper()
        self.printer.print_lower(upper_msg)

# Ejemplo
if __name__ == "__main__":
    # Creamos una instancia de la clase Printer
    my_printer = Printer()
    
    # Creamos el adaptador pasándole la impresora
    adapter = Adapter(my_printer)
    
    # Probamos el método original
    print("Probando método original (print_lower):")
    my_printer.print_lower("Hola Mundo")
    
    # Probamos el adaptador
    print("\nProbando adaptador (print_upper):")
    adapter.print_upper("Hola Mundo")
    
    # Probamos con otro texto
    print("\nProbando con otro texto:")
    adapter.print_upper("El Patrón Adapter es útil")