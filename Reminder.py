import re
import time
import pygame
from datetime import datetime, timedelta


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


def remind_in(text):

    hour = 0
    minute = 0
    second = 0

    # Extracting the hours and minutes and seconds
    hour_pattern = r"(\d+) hour(?:s)?"
    minute_pattern = r"(\d+) minute(?:s)?"
    second_pattern = r"(\d+) second(?:s)?"

    hour_match = re.search(hour_pattern, text)
    minute_match = re.search(minute_pattern, text)
    second_match = re.search(second_pattern, text)

    if hour_match:
        hour = int(hour_match.group(1))
    if minute_match:
        minute = int(minute_match.group(1))
    if second_match:
        second = int(second_match.group(1))

    
    future_time = datetime.now() + timedelta(hours=hour, minutes=minute, seconds=second)
    time_to_remind = future_time.strftime('%H:%M:%S')

    pygame.init()
    pygame.mixer.init()

    while True:
        current_time = datetime.now().strftime('%H:%M:%S')
        if (current_time == time_to_remind):
            pygame.mixer.music.load("C:\\Users\\User\\Desktop\\Assistant\\Assistant\\Sound.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            break
        time.sleep(1)


    

