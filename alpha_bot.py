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
        return "Hey There ๐"

    if message in ("who are you", "who are you?", "who are you ?"):
        return "My name is alpha.\nI am Red Alpha's Assistant ๐\n*Drop your message here, I can help you ๐โโ"

    if message in ("time", "time?", "time ?"):
        time = datetime.now()
        time = time.strftime("Time is : %H:%M")
        return str(time)

    if message in ("date", "date?", "date ?"):
        date = datetime.now()
        date = date.strftime("Today is : %d/%m/%y")
        return str(date)

    if message in ("ok"):
        return "ok โ"

    if message in ("thank", "thank you", "thanks"):
        return "Welcome ๐"

    if message in ("bye", "bye bye", "see you"):
        return "Bye bye ๐ค\nHave a wonderful or great day โจ"

    if message in ("alpha", "red alpha", "redalpha", "red alpha?", "red alpha ?"):
        return "Yes, I am stay ๐ you want help ?"

    # Details Bot ------------------------------------------------------------------------------------------------------
    if message in ("how old are you", "how old are you?", "how old are you ?"):
        return "2 Days ๐"

    if message in ("where you from", "where you from?", "where you from ?"):
        return "I am from Sri Lanka"

    if message in ("help", "help?", "i need help"):
        return "ok tell me your problem "

    return "I don't understand you ๐คจ please tell me again ๐ or contact my creator\n" \
           "Email : minduladilthushan1@gmail.com\n" \
           "Mobile Number : 0741900680"
