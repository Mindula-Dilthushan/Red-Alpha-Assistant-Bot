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

    if message in ("alpha", "red alpha", "redalpha", "red alpha?", "red alpha ?"):
        return "Yes, I am stay 😉 you want help ?"

    # Details Bot ------------------------------------------------------------------------------------------------------
    if message in ("how old are you", "how old are you?", "how old are you ?"):
        return "2 Days 😁"

    if message in ("where you from", "where you from?", "where you from ?"):
        return "I am from Sri Lanka"

    if message in ("help", "help?", "i need help"):
        return "ok tell me your problem "

    return "I don't understand you 🤨 please tell me again 🙃 or contact my creator\n" \
           "Email : minduladilthushan1@gmail.com\n" \
           "Mobile Number : 0741900680"
