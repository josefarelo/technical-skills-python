import asyncio
import random

async def operacion_asincrona(id_tarea):
    await asyncio.sleep(random.uniform(0.1, 1.0))
    if random.random() < 0.3:  # 30% de probabilidad de error
        raise RuntimeError(f"Error en tarea {id_tarea}")
    return f"Tarea {id_tarea} completada"

async def manejar_tarea(id_tarea):
    try:
        resultado = await operacion_asincrona(id_tarea)
        print(resultado)
    except RuntimeError as e:
        print(f"Error manejado: {e}")
    finally:
        print(f"Limpieza para tarea {id_tarea}")

async def ejecutar_tareas():
    tareas = [manejar_tarea(i) for i in range(5)]
    await asyncio.gather(*tareas)
    print("Todas las tareas finalizadas")

async def main():
    print("Iniciando programa asíncrono")
    try:
        await ejecutar_tareas()
    except Exception as e:
        print(f"Error crítico: {e}")
    finally:
        print("Programa terminado")

if __name__ == "__main__":
    asyncio.run(main())