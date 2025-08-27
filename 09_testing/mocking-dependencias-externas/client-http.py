import requests

def obtener_json(url: str):
    try:
        resp = requests.get(url, timeout=3)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos: {e}")
        return None