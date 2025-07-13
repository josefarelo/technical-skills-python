class Maybe:
    def __init__(self, value):
        self.value = value
    
    def bind(self, func):
        try:
            if self.value is None:
                return Maybe(None)
            result = func(self.value)
            return Maybe(result)
        except Exception as e:
            print(f"Error: {e}")
            return Maybe(None)
    
    def get_value(self):
        return self.value
    
    def __str__(self):
        return f"Maybe({self.value})"

# Ejemplos
# Caso exitoso
print("-- Caso exitoso --")
result1 = Maybe(10).bind(lambda x: x * 3).bind(lambda x: x - 5)
print(result1)  # Maybe(25)

# Caso con None
print("\n-- Caso con None --")
result2 = Maybe(None).bind(lambda x: x + 2)
print(result2)  # Maybe(None)

# Caso con error
print("\n-- Caso con error --")
result3 = Maybe("texto").bind(lambda x: x.upper()).bind(lambda x: x / 2)
print(result3)  # Error y Maybe(None)

# Caso encadenado más complejo
print("\n-- Caso encadenado --")
def add_five(x):
    return x + 5

def square(x):
    return x * x

result4 = Maybe(2).bind(add_five).bind(square).bind(lambda x: x / 2)
print(result4)  # Maybe(24.5)