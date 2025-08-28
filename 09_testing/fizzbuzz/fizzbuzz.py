def fizzbuzz(n: int) -> str:
    if n == 0:
        raise ValueError("El número no puede ser cero")
    
    resultado = ""
    
    if n % 3 == 0:
        resultado += "Fizz"
    
    if n % 5 == 0:
        resultado += "Buzz"
    
    if resultado == "":
        resultado = str(n)
    
    return resultado