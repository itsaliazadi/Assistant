import os
from gtts import gTTS
from playsound import playsound

def text_to_speech(text, language='en', slow=False):
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save("output.mp3")
    try:
        playsound("output.mp3")
    finally:
        os.remove("output.mp3")

