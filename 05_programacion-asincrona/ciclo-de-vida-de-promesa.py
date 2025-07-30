import asyncio

async def check_future_status(future, name):
    while not future.done():
        print(f"Future '{name}' todavía está pendiente...")
        await asyncio.sleep(0.3)
    print(f"Future '{name}' completado!")

async def set_future_result(future, value, delay):
    await asyncio.sleep(delay)
    future.set_result(value)
    print(f"Resultado '{value}' establecido después de {delay} segundos")

async def main():
    # Crear dos futures diferentes
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    # Tareas para monitorear los estados
    monitor1 = asyncio.create_task(check_future_status(future1, "Tarea rápida"))
    monitor2 = asyncio.create_task(check_future_status(future2, "Tarea lenta"))

    # Tareas para establecer resultados
    setter1 = asyncio.create_task(set_future_result(future1, "Rápido", 1))
    setter2 = asyncio.create_task(set_future_result(future2, "Lento", 3))

    # Esperar a que todos los futures estén completos
    await asyncio.gather(future1, future2)

    # Mostramos resultados finales
    print("\nEstados finales:")
    print(f"Future1 - done: {future1.done()}, result: {future1.result()}")
    print(f"Future2 - done: {future2.done()}, result: {future2.result()}")

    # Cancelar los monitores (por si acaso)
    monitor1.cancel()
    monitor2.cancel()

    # Limpieza
    try:
        await asyncio.gather(monitor1, monitor2, return_exceptions=True)
    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    asyncio.run(main())