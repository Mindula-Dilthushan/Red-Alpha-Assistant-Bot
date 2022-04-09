# Project   : Red Alpha Assistant Bot
# Author    : Mindula Dilthushan
# Email     : minduladilthushan1@gmail.com
# Date      : 22/04/09

from datetime import datetime

def basic_messages(input_text):
    message = str(input_text).lower()

    if message in ("hello", "hi", "bro"):
        return "Hey! "

    if message in ("who are you", "who are you?"):
        return "My name is alpha.\nI am Red Alpha's Assistant,\n*Drop your message here,I can help you"

    if message in ("time", "time?", "time ?"):
        time = datetime.now()
        time = time.strftime("Time is : %H:%M")
        return str(time)

    if message in ("date", "date?", "date ?"):
        date = datetime.now()
        date = date.strftime("Today is : %d/%m/%y")
        return str(date)

    return "I don't understand you, please tell me again"
