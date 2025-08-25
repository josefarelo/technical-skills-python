import pytest
from texto import es_palindromo

@pytest.mark.parametrize("entrada,esperado", [
    ("reconocer", True),
    ("Anita lava la tina", True),
    ("Python", False),
    ("", True),
    ("12321", True),
    ("hola mundo", False),
    ("A man a plan a canal Panama", True),
    ("Was it a car or a cat I saw?", True),
    ("not a palindrome", False),
    ("A", True),
    ("Aa", True),
    ("Ab", False),
])
def test_es_palindromo(entrada, esperado):
    resultado = es_palindromo(entrada)
    assert resultado == esperado, f"Para '{entrada}' se esperaba {esperado} pero se obtuvo {resultado}"


def test_es_palindromo_con_numeros():
    assert es_palindromo("12321") == True
    assert es_palindromo("12345") == False


def test_es_palindromo_con_caracteres_especiales():
    assert es_palindromo("¡A man, a plan, a canal - Panama!") == True
    assert es_palindromo("Hello, World!") == False


if __name__ == "__main__":
    # Algunos tests básicos para correr sin pytest
    print("Probando la función es_palindromo:")
    test_cases = [
        ("reconocer", True),
        ("Python", False),
        ("", True),
        ("Anita lava la tina", True)
    ]
    
    for texto, esperado in test_cases:
        resultado = es_palindromo(texto)
        estado = "✓" if resultado == esperado else "✗"
        print(f"{estado} '{texto}' -> {resultado} (esperado: {esperado})")
