# 🎙️ AI Voice Translator — Intérprete y Traductor de Voz en Tiempo Real

> Aplicación web full-stack desarrollada con **FastAPI** en el backend y un frontend HTML5/JavaScript interactivo, diseñada para la transcripción, traducción e interpretación de voz en tiempo real.

---

## 🚀 Descripción del Proyecto

Esta aplicación permite capturar audio nativo desde el navegador en español, enviarlo a un servidor backend para su procesamiento mediante modelos avanzados de reconocimiento de voz (**Speech-to-Text**), traducirlo al inglés y generar automáticamente la respuesta hablada mediante síntesis de voz (**Text-to-Speech**).

El proyecto está estructurado con una arquitectura cliente-servidor robusta, lista para despliegues en servidores de producción (como VPS en DonWeb) o ejecución mediante contenedores.

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (API de alto rendimiento para el procesamiento de peticiones).
- **Frontend:** HTML5, CSS3 y JavaScript nativo (captura de audio con `MediaRecorder API` y reproductor dinámico).
- **Speech-to-Text (STT):** `faster-whisper` (Transcripción de alta precisión basada en OpenAI Whisper).
- **Traducción:** API de traducción integrada en el pipeline.
- **Text-to-Speech (TTS):** `edge-tts` (Síntesis de voz natural y fluida en tiempo real).
- **Procesamiento de Audio:** `soundfile` y `numpy`.

---

## ✨ Características Principales

1. **Captura Web Nativa:** Grabación directa desde el micrófono del navegador o subida de archivos de audio (`.wav` / audio genérico).
2. **Pipeline de IA Integrado:** Transcripción, traducción y síntesis ejecutadas de forma secuencial en el backend.
3. **Interfaz Moderna y Limpia:** Diseño responsivo con componentes modulares y sección de agradecimientos a patrocinadores.
4. **Seguridad en Enlaces:** Implementación de buenas prácticas web (`target="_blank" rel="noopener noreferrer"`).

---

## 📁 Estructura del Repositorio

```text
voice-to-voice-translator/
│
├── utils/            # Recursos gráficos y logos de patrocinadores
├── main.py           # Servidor principal y rutas de FastAPI
├── index.html        # Interfaz de usuario web
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Documentación del proyecto

⚙️ Ejecución Local
Clonar el repositorio:

1.Clonar el repositorio:
git clone [https://github.com/marhermac/voice-to-voice-translator.git](https://github.com/marhermac/voice-to-voice-translator.git)
cd voice-to-voice-translator

2.Crear y activar el entorno virtual:
python -m venv .venv
.\.venv\Scripts\Activate.ps1

3.Instalar las dependencias:
pip install -r requirements.txt

4.Ejecutar el servidor local con Uvicorn:
uvicorn main:app --reload
Abrir en el navegador:
Ingresá a http://127.0.0.1:8000 para interactuar con la aplicación.
