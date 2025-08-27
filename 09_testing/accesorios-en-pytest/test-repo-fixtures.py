import pytest
from repo import RepoMemoria

@pytest.fixture
def repo():
    return RepoMemoria()

@pytest.fixture
def repo_con_datos():
    repo = RepoMemoria()
    repo.guardar("u1", {"nombre": "Ana", "edad": 25})
    repo.guardar("u2", {"nombre": "Luis", "edad": 30})
    repo.guardar("u3", {"nombre": "Maria", "edad": 28})
    return repo

def test_guardar_y_obtener(repo):
    repo.guardar("u1", {"nombre": "Ana"})
    resultado = repo.obtener("u1")
    assert resultado == {"nombre": "Ana"}
    assert resultado["nombre"] == "Ana"

def test_clave_inexistente_devuelve_none(repo):
    resultado = repo.obtener("no_existe")
    assert resultado is None

def test_obtener_todo_vacio(repo):
    todo = repo.obtener_todo()
    assert todo == {}
    assert len(todo) == 0

def test_obtener_todo_con_datos(repo_con_datos):
    todo = repo_con_datos.obtener_todo()
    assert len(todo) == 3
    assert "u1" in todo
    assert "u2" in todo
    assert "u3" in todo
    assert todo["u1"]["nombre"] == "Ana"

def test_sobrescribir_valor(repo_con_datos):
    repo_con_datos.guardar("u1", {"nombre": "Ana Modificada", "edad": 26})
    resultado = repo_con_datos.obtener("u1")
    assert resultado["nombre"] == "Ana Modificada"
    assert resultado["edad"] == 26

def test_guardar_nuevo_valor(repo_con_datos):
    repo_con_datos.guardar("u4", {"nombre": "Carlos", "edad": 22})
    resultado = repo_con_datos.obtener("u4")
    assert resultado is not None
    assert resultado["nombre"] == "Carlos"