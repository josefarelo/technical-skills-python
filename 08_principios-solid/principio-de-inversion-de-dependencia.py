from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class EmailNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}")
        # Aquí iría el código real para enviar email
        # con alguna librería como smtplib

class SMSNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")
        # Código para enviar SMS con alguna API
        # de un servicio de mensajería

class PushNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Enviando notificación push: {mensaje}")
        # Implementación para notificaciones push
        # a dispositivos móviles

class ServicioAlerta:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador
        self.historial = []  # Para guardar historial de alertas

    def alerta(self, mensaje):
        try:
            self.notificador.enviar(mensaje)
            self.historial.append({"mensaje": mensaje, "estado": "enviado"})
            print("Alerta enviada correctamente")
        except Exception as e:
            print(f"Error enviando alerta: {e}")
            self.historial.append({"mensaje": mensaje, "estado": "fallido"})

    def mostrar_historial(self):
        print("\nHistorial de alertas:")
        for i, alerta in enumerate(self.historial, 1):
            print(f"{i}. {alerta['mensaje']} - {alerta['estado']}")

# Ejemplo
if __name__ == "__main__":
    # Crear diferentes tipos de notificadores
    notificador_email = EmailNotificador()
    notificador_sms = SMSNotificador()
    notificador_push = PushNotificador()
    
    # Servicio de alertas con email
    alerta_service = ServicioAlerta(notificador_email)
    alerta_service.alerta("Servidor caído - revisar inmediatamente")
    
    # Cambiar a SMS sin modificar el servicio
    alerta_service.notificador = notificador_sms
    alerta_service.alerta("Base de datos no responde")
    
    # Cambiar a notificaciones push
    alerta_service.notificador = notificador_push
    alerta_service.alerta("Sistema recuperado - todo normal")
    
    # Mostrar historial
    alerta_service.mostrar_historial()