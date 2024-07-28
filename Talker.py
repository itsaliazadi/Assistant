import os
from gtts import gTTS
from playsound import playsound

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    try:
        playsound("output.mp3")
    finally:
        os.remove("output.mp3")

