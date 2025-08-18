class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class CalculadoraSalarios:
    def calcular_total(self, empleados):
        try:
            if not empleados:
                raise ValueError("La lista de empleados está vacía")
            
            if not all(isinstance(e, Empleado) for e in empleados):
                raise TypeError("Todos los elementos deben ser Empleados")
                
            return sum(e.salario for e in empleados)
        except Exception as e:
            print(f"Error en cálculo: {e}")
            return 0

class ReporteSalarios:
    def imprimir_reporte(self, total):
        try:
            if not isinstance(total, (int, float)):
                raise TypeError("El total debe ser numérico")
                
            print("\n--- REPORTE DE SALARIOS ---")
            print(f"Total de salarios: ${total:.2f}")
            print("--------------------------\n")
        except Exception as e:
            print(f"Error al imprimir reporte: {e}")

# Ejemplo
if __name__ == "__main__":
    empleados = [
        Empleado("Juan", 2500.50),
        Empleado("Ana", 3200.75),
        Empleado("Luis", 1800.00)
    ]
    
    calculadora = CalculadoraSalarios()
    total = calculadora.calcular_total(empleados)
    
    reporte = ReporteSalarios()
    reporte.imprimir_reporte(total) 