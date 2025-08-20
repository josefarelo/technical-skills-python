class Ave:
    def hacer_sonido(self):
        return "Esta ave hace un sonido."
    
    def mover(self):
        return "Esta ave se está moviendo."

class AveVoladora(Ave):
    def volar(self):
        return "Esta ave está volando alto en el cielo."
    
    def mover(self):
        return self.volar()

class AveNoVoladora(Ave):
    def caminar(self):
        return "Esta ave está caminando en el suelo."
    
    def mover(self):
        return self.caminar()

class Aguila(AveVoladora):
    def hacer_sonido(self):
        return "¡Kiiiiii!"
    
    def cazar(self):
        return "El águila está cazando presas."

class Pinguino(AveNoVoladora):
    def hacer_sonido(self):
        return "¡Ork ork!"
    
    def nadar(self):
        return "El pingüino está nadando en el agua fría."

class Pato(AveVoladora):
    def hacer_sonido(self):
        return "¡Cuac cuac!"
    
    def nadar(self):
        return "El pato está nadando en el lago."

# Ejemplo
def mostrar_comportamiento(ave):
    print(f"Tipo de ave: {type(ave).__name__}")
    print(f"Sonido: {ave.hacer_sonido()}")
    print(f"Movimiento: {ave.mover()}")
    
    if isinstance(ave, AveVoladora):
        print(f"Vuelo: {ave.volar()}")
    elif isinstance(ave, AveNoVoladora):
        print(f"Caminar: {ave.caminar()}")
    
    if isinstance(ave, Aguila):
        print(f"Caza: {ave.cazar()}")
    elif isinstance(ave, Pinguino):
        print(f"Nadar: {ave.nadar()}")
    elif isinstance(ave, Pato):
        print(f"Nadar: {ave.nadar()}")
    
    print("-" * 40)

# Probar el código
aves = [
    Aguila(),
    Pinguino(),
    Pato()
]

for ave in aves:
    mostrar_comportamiento(ave)