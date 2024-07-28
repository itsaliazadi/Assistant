import Talker
import Weather
import Reminder
import Wikipedia
import threading
import customtkinter as ctk
import tkinter as tk
import speech_recognition as sr
import InputHandler


class AssistantGui(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.title("Assistant")
        self.geometry("600x500")

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")

        self.label = ctk.CTkLabel(self, text="Speak something", font=("Times New Roman", 30), width=560, height=40)
        self.label.place(x=25, y=50)

        self.statusButton = ctk.CTkButton(self, text="Start", command=self.startListening, width=200, height=40, font=("Times New Roman", 24))
        self.statusButton.place(x=200, y=200)

        self.guide_frame = ctk.CTkFrame(self, width=500, height=50, corner_radius=10)
        self.guide_frame.place(x=50, y=300)

        self.guide_title = ctk.CTkLabel(self.guide_frame, text="How to use", font=("Times New Roman", 18), width=450, height=40)
        self.guide_title.place(x=25, y=5)

        self.guide_button = ctk.CTkButton(self.guide_frame, text="Show details", command=self.show_guide_details, width=100, height=30, font=("Times New Roman", 14))
        self.guide_button.place(x=400, y=10)

        self.guide_details = ctk.CTkLabel(self, text="1. Click the 'Start' button to begin listening.\n2. Speak your question or command clearly.\n3. The assistant will process your input and respond accordingly.", font=("Times New Roman", 14), width=450, height=150, justify=tk.LEFT)
        self.guide_details.place(x=50, y=350)
        self.guide_details.pack_forget()  # hide the guide details initially

        self.processing_question = False

    def startListening(self) ->None:
        self.processing_question = True
        self.statusButton.configure(text="Listenning...")
        threading.Thread(target=self.processAudio).start()

    def processAudio(self) ->None:
        InputHandler.handleInput()
        self.processing_question = False
        self.statusButton.configure(text="Start")

    def show_guide_details(self):
        if self.guide_button.cget("text") == "Show details":
            self.guide_button.configure(text="Hide details")
            self.guide_details.pack()  # show the guide details
        else:
            self.guide_button.configure(text="Show details")
            self.guide_details.pack_forget()  # hide the guide details