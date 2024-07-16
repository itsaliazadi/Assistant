# Simple Virtual Assistant: Create a simple virtual assistant that can perform tasks like setting reminders, sending emails, or making phone calls. You could use Python's speech recognition and text-to-speech libraries for this project.

import re
import time
from datetime import datetime
import pygame




def set_alarm_clock(text):

    time_to_remind = ""

    # Extracting the time
    pattern = r"for (\d{1,2}:\d{2})"
    match = re.search(pattern, text)
    time_string = match.group(1)
    
    # Converting the time into the standard form
    if "p.m" in text:
        time_string += " pm"
        dt = datetime.strptime(time_string, "%I:%M %p")
        standard_time_string = dt.strftime("%H:%M")
        time_to_remind = standard_time_string

    else:
        time_to_remind = time_string



    pygame.init()
    pygame.mixer.init()
    while True:
        current_time = datetime.now().strftime('%H:%M')
        if current_time == time_to_remind:
            pygame.mixer.music.load("C:\\Users\\User\\Desktop\\Assistant_project\\Assistant\\Sound.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            break
        time.sleep(1)



