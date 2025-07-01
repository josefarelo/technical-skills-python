def dividir_numeros():
    print("Calculadora de división")
    print("-----------------------")
    
    try:
        # Pedir números al usuario
        num1 = int(input("Ingresa el primer número (numerador): "))
        num2 = int(input("Ingresa el segundo número (denominador): "))
        
        # Realizar la división
        resultado = num1 / num2
        
        # Mostrar resultado
        print(f"\nEl resultado de dividir {num1} entre {num2} es: {resultado:.2f}")
    
    except ZeroDivisionError:
        print("\n¡Error! No se puede dividir entre cero. Intenta con otro número.")
    
    except ValueError:
        print("\n¡Error! Debes ingresar números enteros válidos.")
    
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
    
    finally:
        print("\nGracias por usar la calculadora de división. ¡Hasta luego!")

# Llamar a la función
dividir_numeros()