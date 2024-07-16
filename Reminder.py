# Simple Virtual Assistant: Create a simple virtual assistant that can perform tasks like setting reminders, sending emails, or making phone calls. You could use Python's speech recognition and text-to-speech libraries for this project.


import time
import datetime
import pygame




def set_alarm_clock(time_to_remind, task):
    pygame.init()
    pygame.mixer.init()
    while True:
        current_time = datetime.datetime.now().strftime('%H:%M')
        if current_time == time_to_remind:
            pygame.mixer.music.load("C:\\Users\\User\\Desktop\\Assistant_project\\Assistant\\Sound.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            break
        time.sleep(1)



