class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized') or not self._initialized:
            self.logs = []
            self._initialized = True

    def log(self, message):
        log_entry = f"[LOG]: {message}"
        self.logs.append(log_entry)
        print(log_entry)

    def show_logs(self):
        print("\n--- Log History ---")
        for log in self.logs:
            print(log)
        print("------------------\n")

# Ejemplo
logger1 = Logger()
logger1.log("Starting application")
logger1.log("Loading configuration")

logger2 = Logger()
logger2.log("User logged in")

print(f"Are both instances the same? {logger1 is logger2}")

logger1.show_logs()