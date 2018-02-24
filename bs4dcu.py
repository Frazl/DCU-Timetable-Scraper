from bs4 import BeautifulSoup
import requests
import configfraz
import dcudates
import warnings
warnings.filterwarnings("ignore")

times = configfraz.times

days = configfraz.days

def getdays(x):
    days_id = []
    for i in range(0, len(x)):
        c = x[i].get_text().split("\n")
        if c[1] in days:
            xstring = str(x[i])
            rowspan = xstring.split("rowspan")[1][2]
            rowspan = int(rowspan)
            days_id.append([i])
            prevadditional = 0
            for iii in range(rowspan-1):
                toincrease = xstring.count("<tr")
                if prevadditional == 0:
                    additional = i + toincrease
                else:
                    additional = toincrease + prevadditional

                xstring = str(x[additional])
                prevadditional = additional
                days_id[len(days_id) - 1].append(additional)
    return days_id

def timetableparser(x, i, day, data):
    i = i
    t = 2 
    le_flag = False
    s = ""
    while i < len(x) and t < 21:
        if le_flag:
            #print("Time:", times[t], s)
            data[day][times[t]].append(s)
            le_flag = False
            t = t + 1
            continue
        if x[i] != "":
            s = x[i+9], "In", x[i+1], "With", x[i+8]
            s = " ".join(str(i) for i in s)
            #print("Time:", times[t], s)
            data[day][times[t]].append(s)
            i = i + 22
            t += 1
            le_flag = True
        else:
            #print("Nothing On At:", times[t])
            i = i + 1
            t = t + 1

def normal(days_id, x):
    data = configfraz.data
    for dayidmini in days_id:
        for i in range(0, len(dayidmini)):
            dayid = dayidmini[i]
            y = x[dayid].get_text().split("\n")
            if y[1] != "":
                day = y[1]
            if i == 0:
                #print("Today is:", day)
                timetableparser(y, 2, day, data)
            else:
                timetableparser(y, 1, day, data)
    return data

def run(day, time=False, code="CA"):
    page = requests.get("https://www101.dcu.ie/timetables/feed.php?prog="+code+"&per=1&week1=20&week2=31&hour=1-20&template=student", verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    x = soup.find_all("tr")
    days_id = getdays(x)
    all_data = normal(days_id, x)
    if time:
        return all_data[day][time]
    else:
        return all_data[day]

def beautify(datacontent):
    s = ""
    if type(datacontent) == dict:
        for key in datacontent.keys():
            for x in datacontent[key]:
                s = s + "---" + x
            if s == "":
                s = "Nothing"
            print("At", key, "There is", s)
            s = ""
    elif type(datacontent) == list:
        if len(datacontent) < 1:
            print("Nothing")
        for x in datacontent:
            print(x)

def next():
    day = dcudates.getday()
    time = dcudates.nexttime()
    if time in days:
        print(time)
        print(beautify(run(time)))
    else:
        print(beautify(run(day, time)))
def main():
    while True:
        print("Enter a Day")
        day = input()
        if day == "next":
            next()
            continue
        if day not in days:
            print("Warning: Day not valid if entered")
        print("Enter a time")
        time = input()
        if time not in configfraz.timechecks:
            print("Warning: Time not valid if entered")
        print("Enter a module code")
        code = input()
        print("Fetching results:")

        if time == "":
            time = None
        if day == "":
            day = None
        if code == "":
            code = None

        beautify(run(day, time, code))    

if __name__ == '__main__':
    main()