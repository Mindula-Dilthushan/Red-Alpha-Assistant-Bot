# Project       : Red Alpha Assistant Bot
# Author        : Mindula Dilthushan
# Email         : minduladilthushan1@gmail.com
# Crate Date    : 22/04/09
# Update Date   : 22/04/10

from datetime import datetime

def bot_messages(input_text):
    message = str(input_text).lower()

    # Basic Messages ---------------------------------------------------------------------------------------------------

    if message in ("hello", "hi", "bro"):
        return "Hey There 👋"

    if message in ("who are you", "who are you?", "who are you ?"):
        return "My name is alpha.\nI am Red Alpha's Assistant 😎\n*Drop your message here, I can help you 🙋‍♂"

    if message in ("time", "time?", "time ?"):
        time = datetime.now()
        time = time.strftime("Time is : %H:%M")
        return str(time)

    if message in ("date", "date?", "date ?"):
        date = datetime.now()
        date = date.strftime("Today is : %d/%m/%y")
        return str(date)

    if message in ("ok"):
        return "ok ✌"

    if message in ("thank", "thank you", "thanks"):
        return "Welcome 😊"

    if message in ("bye", "bye bye", "see you"):
        return "Bye bye 🤗\nHave a wonderful or great day ✨"

    if message in ("alpha", "red alpha", "redalpha"):
        return "Yes, I am stay 😉 you want help ? yes or no ?"
    elif message in ("yes", "yess"):
        return "What help do you need ?"
    elif message in ("no", "noo"):
        return "ok ✌"

    # Details Bot ------------------------------------------------------------------------------------------------------







    return "I don't understand you 🤨 please tell me again 🙃"
