import speech_recognition as sr
import Reminder
import threading

# Create a Recognizer instance
recognizer = sr.Recognizer()

reminder_words = ["remind", "alarm", "alert", "notify"]

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


        if (text == "Done" or text == "done"):
            break


    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error: Could not request results from Google Speech Recognition service;")