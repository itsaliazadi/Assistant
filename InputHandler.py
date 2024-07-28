import Talker
import Weather
import Reminder
import Wikipedia
import threading
import customtkinter as ctk
import tkinter as tk
import speech_recognition as sr

reminder_words = ["remind", "alarm", "alert", "notify"]
weather_words = ["weather", "climate"]
wikipedia_words = ["wikipedia", "summary"]


def handleInput():
        recognizer = sr.Recognizer()

        # Capture audio input from the microphone
        with sr.Microphone() as source:
            audio_data = recognizer.listen(source, phrase_time_limit=5)

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
                    threading.Thread(target=Talker.text_to_speech, args=(str(Weather.describeWeather(text)),)).start()
                    break

            # Temperature
            if "temperature" in text:
                threading.Thread(target=Talker.text_to_speech, args=(str(Weather.getTemperature(text)),)).start()

            # Wikipedia
            for word in wikipedia_words:
                if word in text:
                    threading.Thread(target=Talker.text_to_speech, args=(str(Wikipedia.getASummaryOf(text)),)).start()
                    break
        

            if (text == "Done" or text == "done"):
                pass


        except sr.UnknownValueError:
            Talker.text_to_speech("Sorry, could not understand what you said.")
        except sr.RequestError as e:
            print("Error: Could not request results from Google Speech Recognition service;")
