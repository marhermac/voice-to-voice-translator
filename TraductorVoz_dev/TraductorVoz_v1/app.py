from audio.recorder import record_audio
from speech.stt import speech_to_text
from translator.translator import translate_text
from speech.tts import text_to_speech
from audio.player import play_audio


def main():

    print("=" * 40)
    print("TRADUCTOR DE VOZ")
    print("=" * 40)

    archivo = record_audio()

    texto = speech_to_text(archivo)

    print("\nTexto reconocido:")
    print(texto)

    traduccion = translate_text(
        texto,
        source="es",
        target="en"
    )

    print("\nTraducción:")
    print(traduccion)

    voz = text_to_speech(traduccion)

    if voz:
        print("\n🔊 Reproduciendo...")
        play_audio(voz)
    else:
        print("No se pudo reproducir el audio.") 
if __name__ == "__main__":
    main()