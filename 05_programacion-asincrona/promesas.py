import asyncio
import random

async def operacion_asincrona(future):
    await asyncio.sleep(2)  # Simular trabajo asíncrono
    
    # 80% de probabilidad de éxito, 20% de fallo
    if random.random() < 0.8:
        future.set_result("¡Operación completada con éxito!")
    else:
        future.set_exception(Exception("Algo salió mal en la operación"))

async def manejar_future():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    
    # Iniciar la operación asíncrona
    asyncio.create_task(operacion_asincrona(future))
    
    try:
        # Esperar el resultado
        resultado = await future
        print(f"Éxito: {resultado}")
    except Exception as e:
        print(f"Fallo: {str(e)}")
    
    # Mostrar estado final por curiosidad
    print(f"Estado del Future: {'done' if future.done() else 'pending'}")
    if future.done():
        if future.exception() is None:
            print(f"Resultado: {future.result()}")
        else:
            print(f"Excepción: {future.exception()}")

async def main():
    print("--- Iniciando simulación de Promise con Future ---")
    await manejar_future()
    print("--- Simulación completada ---")

if __name__ == "__main__":
    asyncio.run(main())