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
        data = datetime.now()
        date_time = data.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    return "I don't understand you, please tell me again"