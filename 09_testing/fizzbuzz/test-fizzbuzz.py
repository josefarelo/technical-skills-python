import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("numero, resultado_esperado", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (4, "4"),
    (5, "Buzz"),
    (6, "Fizz"),
    (7, "7"),
    (8, "8"),
    (9, "Fizz"),
    (10, "Buzz"),
    (11, "11"),
    (12, "Fizz"),
    (13, "13"),
    (14, "14"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
    (45, "FizzBuzz"),
    (100, "Buzz"),
])
def test_fizzbuzz_con_varios_numeros(numero, resultado_esperado):
    resultado_obtenido = fizzbuzz(numero)
    assert resultado_obtenido == resultado_esperado

def test_fizzbuzz_con_cero():
    try:
        fizzbuzz(0)
        assert False, "Debería haber lanzado una excepción"
    except ValueError:
        assert True

def test_fizzbuzz_con_numero_negativo():
    resultado = fizzbuzz(-3)
    assert resultado == "Fizz"

def test_fizzbuzz_con_numero_grande():
    resultado = fizzbuzz(999)
    assert resultado == "Fizz"