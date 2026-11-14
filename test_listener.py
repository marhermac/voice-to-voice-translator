from audio.listener import Listener

listener = Listener()

audio = listener.listen()

print()

print("Audio capturado")

print(audio.shape)