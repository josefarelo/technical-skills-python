class Subject:
    def __init__(self, name):
        self.name = name
        self.observers = []
        self._state = None

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
            print(f"{observer.name} añadido como observador de {self.name}")
        else:
            print(f"{observer.name} ya está observando a {self.name}")

    def remove_observer(self, observer):
        try:
            self.observers.remove(observer)
            print(f"{observer.name} eliminado de {self.name}")
        except ValueError:
            print(f"{observer.name} no estaba observando a {self.name}")

    def notify(self):
        for observer in self.observers:
            observer.update(self._state)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state
        print(f"{self.name} cambió su estado a: {self._state}")
        self.notify()

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} recibió actualización: {message}")

# Ejemplo
if __name__ == "__main__":
    # Crear sujeto
    weather_station = Subject("Estación Meteorológica")

    # Crear observadores
    phone_app = Observer("App Móvil")
    tv_display = Observer("Pantalla TV")
    web_service = Observer("Servicio Web")

    # Registrar observadores
    weather_station.add_observer(phone_app)
    weather_station.add_observer(tv_display)
    weather_station.add_observer(web_service)

    # Cambiar estado (notifica automáticamente)
    weather_station.state = "25°C y soleado"
    print("---")

    # Eliminar un observador
    weather_station.remove_observer(tv_display)

    # Nuevo cambio de estado
    weather_station.state = "18°C y lluvioso"