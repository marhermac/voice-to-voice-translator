from deep_translator import GoogleTranslator


def translate_text(texto, source="es", target="en"):

    traduccion = GoogleTranslator(
        source=source,
        target=target
    ).translate(texto)

    return traduccion