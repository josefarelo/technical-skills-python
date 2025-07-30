import asyncio
import time

async def tarea(id, delay):
    print(f"[{time.strftime('%X')}] Tarea {id} iniciada")
    await asyncio.sleep(delay)
    print(f"[{time.strftime('%X')}] Tarea {id} completada después de {delay} segundos")

async def tarea_especial():
    print(f"\n[{time.strftime('%X')}] Tarea especial empezando (más larga)")
    await asyncio.sleep(2)
    print(f"[{time.strftime('%X')}] Tarea especial terminada\n")

async def main():
    print(f"\n[{time.strftime('%X')}] Iniciando event loop...")
    
    # Ejecutar tareas normales y especial concurrentemente
    await asyncio.gather(
        tarea(1, 1.5),
        tarea(2, 1),
        tarea(3, 0.5),
        tarea_especial()
    )
    
    print(f"\n[{time.strftime('%X')}] Todas las tareas completadas!")

if __name__ == "__main__":
    asyncio.run(main())