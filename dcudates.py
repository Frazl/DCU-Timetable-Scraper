import datetime
import configfraz

def getday():
    now = datetime.datetime.now()
    today = now.strftime("%A")[:3]
    today = today
    return today

def gettomorrow():
    today = int(datetime.datetime.now().weekday())
    if today != 6:
        today = today + 1
    else:
        today = 0 
    return configfraz.days[today]


def nexttime():
    now = datetime.datetime.now()
    hour = int(now.strftime("%H"))
    minute = int(now.strftime("%M"))
    if hour > 17:
        s = gettomorrow()
        return s
    else:
        if minute >= 30:
            minute = 30
        else:
            minute = 0
        s = str(hour)+":"+str(minute)+"0"
        return s