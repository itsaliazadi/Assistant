import speech_recognition as sr

# Create a Recognizer instance
recognizer = sr.Recognizer()

reminder_words = ["remind", "alarm", "alert", "notify"]

while True:
    # Capture audio input from the microphone
    with sr.Microphone() as source:
        print("Speak something...")
        audio_data = recognizer.listen(source, phrase_time_limit=10)

    # Perform speech recognition using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data)

        # Reminder
        for word in reminder_words:
            if word in text:
                # Remind in
                if "in" in text:
                    print("in...")
                # Alarm clock
                else:
                    print(text)
                break


        if (text == "Done" or text == "done"):
            break


    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error: Could not request results from Google Speech Recognition service;")