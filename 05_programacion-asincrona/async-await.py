import asyncio
import random

async def descargar_archivo(nombre_archivo):
    print(f"Descargando {nomobre_archivo}...")
    tiempo_descarga = random.uniform(0.5, 3.0)
    await asyncio.sleep(tiempo_descarga)
    print(f"{nomobre_archivo} descargado en {tiempo_descarga:.2f} segundos!")
    return f"Contenido de {nomobre_archivo}"

async def main():
    archivos = ["foto.jpg", "documento.pdf", "musica.mp3"]
    
    print("Iniciando descargas...")
    tareas = [descargar_archivo(archivo) for archivo in archivos]
    
    try:
        resultados = await asyncio.gather(*tareas)
        print("\nTodas las descargas completadas!")
        for resultado in resultados:
            print(f"- {resultado}")
    except Exception as e:
        print(f"Error durante las descargas: {e}")
    
    print("Proceso terminado.")

if __name__ == "__main__":
    print("=== Simulador de descargas ===")
    asyncio.run(main())