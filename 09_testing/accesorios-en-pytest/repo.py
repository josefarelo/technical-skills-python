class RepoMemoria:
    def __init__(self):
        self.db = {}
    
    def guardar(self, clave, valor):
        self.db[clave] = valor
    
    def obtener(self, clave):
        return self.db.get(clave)
    
    def obtener_todo(self):
        return self.db.copy()