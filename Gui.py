import Talker
import Weather
import Reminder
import threading
import customtkinter as ctk
import tkinter as tk
import speech_recognition as sr

reminder_words = ["remind", "alarm", "alert", "notify"]
weather_words = ["weather", "climate"]


class AssistantGui(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.title("Assistant")
        self.geometry("600x500")

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")

        self.label = ctk.CTkLabel(self, text="Speak something", font=("Times New Roman", 30), width=560, height=40)
        self.label.place(x=25, y=50)
        # self.label.pack()

        self.button = ctk.CTkButton(self, text="Start", command=self.startListening, width=200, height=40, font=("Times New Roman", 24))
        self.button.place(x=200, y=200)
        # self.button.pack()

        self.processing_question = False

    def startListening(self):
        self.processing_question = True
        self.button.configure(text="Listenning...")
        threading.Thread(target=self.processAudio).start()

    def processAudio(self):
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
        

            if (text == "Done" or text == "done"):
                pass


        except sr.UnknownValueError:
            Talker.text_to_speech("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Error: Could not request results from Google Speech Recognition service;")


        self.processing_question = False
        self.button.configure(text="Start")