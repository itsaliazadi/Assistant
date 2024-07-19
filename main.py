import speech_recognition as sr
<<<<<<< HEAD
=======
import Reminder
import threading
>>>>>>> Reminder

# Create a Recognizer instance
recognizer = sr.Recognizer()

reminder_words = ["remind", "alarm", "alert", "notify"]

while True:
    # Capture audio input from the microphone
    with sr.Microphone() as source:
        print("Speak something...")
<<<<<<< HEAD
        audio_data = recognizer.listen(source, phrase_time_limit=10)
=======
        audio_data = recognizer.listen(source, phrase_time_limit=5)
>>>>>>> Reminder

    # Perform speech recognition using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data)
<<<<<<< HEAD
=======
        print(f"You said:{text}")
>>>>>>> Reminder

        # Reminder
        for word in reminder_words:
            if word in text:
                # Remind in
                if "in" in text:
<<<<<<< HEAD
                    print("in...")
                # Alarm clock
                else:
                    print(text)
=======
                    threading.Thread(target=Reminder.remind_in, args=(text,)).start()
                # Alarm clock
                else:
                    threading.Thread(target=Reminder.set_alarm_clock, args=(text,)).start()
>>>>>>> Reminder
                break


        if (text == "Done" or text == "done"):
            break


    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error: Could not request results from Google Speech Recognition service;")