class RealService:
    def fetch(self):
        print("Consultando recurso real... Esto puede ser lento!")
        return "datos_reales_importantes"

class ProxyService:
    def __init__(self):
        self.cache = None
        self.service = RealService()
        self.access_count = 0

    def fetch(self):
        self.access_count += 1
        print(f"Intento de acceso n° {self.access_count}")
        
        if self.cache is None:
            print("Cache vacío, consultando servicio real...")
            self.cache = self.service.fetch()
            print("Datos almacenados en cache!")
        else:
            print("Datos obtenidos desde cache (rápido!)")
        
        return self.cache

# Demo básica
if __name__ == "__main__":
    proxy = ProxyService()
    
    print("\nPrimer acceso:")
    print("Resultado:", proxy.fetch())
    
    print("\nSegundo acceso:")
    print("Resultado:", proxy.fetch())
    
    print("\nTercer acceso:")
    print("Resultado:", proxy.fetch())