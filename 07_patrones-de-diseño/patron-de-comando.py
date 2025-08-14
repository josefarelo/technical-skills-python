class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.encendido = False
    
    def encender(self):
        if not self.encendido:
            print(f"{self.nombre}: Encendiendo...")
            self.encendido = True
        else:
            print(f"{self.nombre}: Ya está encendido")
    
    def apagar(self):
        if self.encendido:
            print(f"{self.nombre}: Apagando...")
            self.encendido = False
        else:
            print(f"{self.nombre}: Ya está apagado")

class Comando:
    def ejecutar(self):
        pass

class EncenderComando(Comando):
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo
    
    def ejecutar(self):
        self.dispositivo.encender()

class ApagarComando(Comando):
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo
    
    def ejecutar(self):
        self.dispositivo.apagar()

class ControlRemoto:
    def __init__(self):
        self.comandos = []
    
    def agregar_comando(self, comando):
        self.comandos.append(comando)
    
    def ejecutar_comandos(self):
        for comando in self.comandos:
            comando.ejecutar()
        self.comandos = []

# Ejemplo
if __name__ == "__main__":
    lampara = Dispositivo("Lámpara del salón")
    tv = Dispositivo("Televisor")
    
    encender_lampara = EncenderComando(lampara)
    apagar_lampara = ApagarComando(lampara)
    encender_tv = EncenderComando(tv)
    apagar_tv = ApagarComando(tv)
    
    control = ControlRemoto()
    
    print("-- Encendiendo dispositivos --")
    control.agregar_comando(encender_lampara)
    control.agregar_comando(encender_tv)
    control.ejecutar_comandos()
    
    print("\n-- Apagando dispositivos --")
    control.agregar_comando(apagar_lampara)
    control.agregar_comando(apagar_tv)
    control.ejecutar_comandos()
    
    print("\n-- Intentando apagar ya apagado --")
    control.agregar_comando(apagar_lampara)
    control.ejecutar_comandos()