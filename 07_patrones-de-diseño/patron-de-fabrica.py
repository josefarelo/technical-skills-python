class Auto:
    def __init__(self):
        self.ruedas = 4
        self.motor = "gasolina"
    
    def conducir(self):
        print("Conduciendo un auto")
    
    def especificaciones(self):
        print(f"Auto - Ruedas: {self.ruedas}, Motor: {self.motor}")

class Moto:
    def __init__(self):
        self.ruedas = 2
        self.motor = "125cc"
    
    def conducir(self):
        print("Conduciendo una moto")
    
    def especificaciones(self):
        print(f"Moto - Ruedas: {self.ruedas}, Motor: {self.motor}")

def vehiculo_factory(tipo):
    vehiculos_disponibles = {
        "auto": Auto,
        "moto": Moto
    }
    
    if tipo.lower() in vehiculos_disponibles:
        return vehiculos_disponibles[tipo.lower()]()
    else:
        raise ValueError(f"Tipo de vehículo no válido. Opciones: {list(vehiculos_disponibles.keys())}")

# Ejemplo
if __name__ == "__main__":
    try:
        mi_auto = vehiculo_factory("auto")
        mi_auto.conducir()
        mi_auto.especificaciones()
        
        mi_moto = vehiculo_factory("moto")
        mi_moto.conducir()
        mi_moto.especificaciones()
        
        # Esto lanzará una excepción
        vehiculo_factory("camion")
    except ValueError as e:
        print(f"Error: {e}")