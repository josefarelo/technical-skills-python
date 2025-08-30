import pytest
from arit import dividir

def test_dividir_ok():
    resultado = dividir(10, 2)
    assert resultado == 5

def test_dividir_otro_numero_ok():
    resultado = dividir(15, 3)
    assert resultado == 5

def test_dividir_por_cero_lanza():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)

def test_dividir_por_cero_mensaje():
    with pytest.raises(ZeroDivisionError) as excinfo:
        dividir(5, 0)
    assert "No se puede dividir por cero" in str(excinfo.value)

def test_dividir_negativos():
    resultado = dividir(-10, 2)
    assert resultado == -5

def test_dividir_decimales():
    resultado = dividir(5.5, 2)
    assert resultado == 2.75