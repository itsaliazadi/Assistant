import speech_recognition as sr
import Reminder
import threading
import Weather
import re
import spacy
import Talker


# Create a Recognizer instance
recognizer = sr.Recognizer()

reminder_words = ["remind", "alarm", "alert", "notify"]
weather_words = ["weather", "climate"]

while True:
    # Capture audio input from the microphone
    with sr.Microphone() as source:
        print("Speak something...")

        audio_data = recognizer.listen(source, phrase_time_limit=5)

    # Perform speech recognition using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data)
        print(f"You said:{text}")

        # Reminder
        for word in reminder_words:
            if word in text:
                # Remind in
                if "in" in text:
                    threading.Thread(target=Reminder.remind_in, args=(text,)).start()
                # Alarm clock
                else:
                    threading.Thread(target=Reminder.set_alarm_clock, args=(text,)).start()
                break

        # Weather
        for word in weather_words:
            if word in text:
                # print(Weather.describeWeather(text))
                threading.Thread(Talker.text_to_speech, args=(Weather.describeWeather(text), )).start()
                # Talker.text_to_speech(f"The weather's condition is:{Weather.describeWeather(text)}")
                break

        # Temperature
        if "temperature" in text:
            # print(Weather.getTemperature(text))
            threading.Thread(Talker.text_to_speech, args=(Weather.getTemperature(text), )).start()
            # Talker.text_to_speech(f"The temperature is:{Weather.getTemperature(text)}")
    



        if (text == "Done" or text == "done"):
            break


    except sr.UnknownValueError:
        # print("Sorry, could not understand audio.")
        Talker.text_to_speech("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error: Could not request results from Google Speech Recognition service;")