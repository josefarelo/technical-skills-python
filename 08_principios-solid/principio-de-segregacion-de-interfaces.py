from abc import ABC, abstractmethod

class RobotCaminanteInterface(ABC):
    @abstractmethod
    def caminar(self):
        pass

class RobotVoladorInterface(ABC):
    @abstractmethod
    def volar(self):
        pass

class RobotNadadorInterface(ABC):
    @abstractmethod
    def nadar(self):
        pass

class RobotBasico(RobotCaminanteInterface):
    def caminar(self):
        return "Robot básico caminando con pasos simples"
    
    def __str__(self):
        return "Robot básico de tierra"

class RobotAvanzado(RobotCaminanteInterface, RobotVoladorInterface):
    def caminar(self):
        return "Robot avanzado caminando con patas articuladas"
    
    def volar(self):
        return "Robot avanzado volando con propulsores"
    
    def __str__(self):
        return "Robot avanzado terrestre y aéreo"

class RobotAcuatico(RobotNadadorInterface):
    def nadar(self):
        return "Robot acuático nadando con aletas"
    
    def __str__(self):
        return "Robot especializado en agua"

# Demostración de uso
if __name__ == "__main__":
    print("Demostración del Principio de Segregación de Interfaces")
    print("=" * 50)
    
    robot1 = RobotBasico()
    print(f"\n{robot1}")
    print(robot1.caminar())
    
    robot2 = RobotAvanzado()
    print(f"\n{robot2}")
    print(robot2.caminar())
    print(robot2.volar())
    
    robot3 = RobotAcuatico()
    print(f"\n{robot3}")
    print(robot3.nadar())
    
    # Verificación de interfaces
    print("\nVerificación de interfaces implementadas:")
    print(f"RobotBásico camina: {hasattr(robot1, 'caminar')}")
    print(f"RobotAvanzado vuela: {hasattr(robot2, 'volar')}")
    print(f"RobotAcuatico nada: {hasattr(robot3, 'nadar')}")
    
    print("\nCada robot implementa solo lo que necesita!")