def es_palindromo(s: str) -> bool:
    limpio = "".join(c.lower() for c in s if c.isalnum())
    return limpio == limpio[::-1]