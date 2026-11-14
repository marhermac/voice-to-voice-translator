import asyncio
import edge_tts
import os

async def main():
    archivo = "audio/temp/prueba.mp3"

    communicate = edge_tts.Communicate(
        "Hello, my name is Mario.",
        "en-US-AndrewNeural"
    )

    await communicate.save(archivo)

    print("¿Existe el archivo?:", os.path.exists(archivo))
    print("Ruta:", os.path.abspath(archivo))

asyncio.run(main())