import random
import os

def toNumberDay(weekday):
    if weekday == "Lunedi'":
        return 1
    if weekday == "Martedi'":
        return 2
    if weekday == "Mercoledi'":
        return 3
    if weekday == "Giovedi'":
        return 4
    if weekday == "Venerdi'":
        return 5
    if weekday == "Sabato":
        return 6
    if weekday == "Domenica":
        return 7

def generator():
    lesson = ["Lunedi' Yoga ore 8",
"Lunedi' Crossfit ore 10",
"Lunedi' Functional ore 12",
"Lunedi' Yoga ore 14",
"Lunedi' Crossfit ore 16",
"Lunedi' Functional ore 18",
"Martedi' Acro Yoga ore 8",
"Martedi' Crossfit Class ore 10",
"Martedi' Functional Class ore 12",
"Martedi' Acro Yoga ore 14",
"Martedi' Crossfit CLass ore 16",
"Martedi' Functional Class ore 18",
"Mercoledi' Yoga ore 8",
"Mercoledi' Crossfit ore 10",
"Mercoledi' Functional ore 12",
"Mercoledi' Yoga ore 14",
"Mercoledi' Crossfit ore 16",
"Mercoledi' Functional ore 18",
"Giovedi' Acro Yoga ore 8",
"Giovedi' Crossfit Class ore 10",
"Giovedi' Functional Class ore 12",
"Giovedi' Acro Yoga ore 14",
"Giovedi' Crossfit Class ore 16",
"Giovedi' Functional Class ore 18",
"Venerdi' Yoga ore 8",
"Venerdi' Crossfit ore 10",
"Venerdi' Functional ore 12",
"Venerdi' Yoga ore 14",
"Venerdi' Crossfit ore 16",
"Venerdi' Functional ore 18"]

    for j in range(25):
        lezione = []
        fout = open(os.path.dirname(__file__) + "/../repo"+"random"+str(j)+'.txt', 'wt')
        for i in range(random.randint(3,15)):
            lezione = random.choice(lesson)
            fout.write(lezione+'\n')
        fout.close()

def datapipeline(reservation):
    for filename in os.listdir(os.path.dirname(__file__) + "/../repo") :
        if filename.startswith("random"):
            try:
                fin = open(os.path.dirname(__file__)+ "/../repo/" + filename, 'rt')
            except FileNotFoundError:
                print('>>> FileNotFound ERROR: check path or exension of file')

            for line in fin:
                lineword = line.split(" ")
                day = toNumberDay(lineword[0])
                hour = int(lineword[len(lineword)-1][:-1])
                in_lesson = ' '.join(str(element) for element in (lineword[1:len(lineword)-2]))
                for lesson in reservation[day]:
                    try:
                        if lesson[hour] == in_lesson:
                            lesson['counter'] = lesson['counter'] + 1
                            break
                    except Exception:
                        pass
        
    return(reservation)

def init():
    reservation={}
    try:
        fin = open(os.path.dirname(__file__) + "/../repo/Corsi.txt", 'rt')
    except (Exception):
        return "ErrorFile"
    
    for lessonLine in fin.readlines():
        if len(lessonLine) > 1:
            lineword = lessonLine.split(" ")
            day = toNumberDay(lineword[0])
            hour = int(lineword[len(lineword)-1])
            lessonName = ' '.join(str(element) for element in (lineword[1:len(lineword)-2]))
            if day in list(reservation.keys()) :
                reservation[day].append({hour:lessonName,'counter':0})
            elif len(list(reservation.keys())) != 0 :
                reservation[day]=[
                                    {hour:lessonName,
                                    'counter':0}
                                ]
            else:
                reservation = { day:[
                                    {hour:lessonName,
                                    'counter':0}
                                ]
                            }
    return reservation


