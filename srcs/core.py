import plot as plt
import requests
import randgen

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

def init():
    reservation={}
    try:
        request = requests.get('http://localhost:60080/lezioni')
    except (Exception):
        return "Error Request:500"
    if request.status_code == 200: 

        for lessonLine in request.text.split("\n"):
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
    else:
        return "BAD Request:400"


def getPrenotated(reservation):
    try:
        request = requests.get('http://localhost:60080/reservation')
    except (Exception):
        return "Error Request:500"
    if request.status_code == 200: 
        for line in request.text.split("\n"):
            if len(line) > 1:
                lineword = line.split(" ")
                day = toNumberDay(lineword[0])
                hour = int(lineword[len(lineword)-1])
                in_lesson = ' '.join(str(element) for element in (lineword[1:len(lineword)-2]))
                for lesson in reservation[day]:
                    try:
                        if lesson[hour] == in_lesson:
                            lesson['counter'] = lesson['counter'] + 1
                            break
                    except Exception:
                        pass
        return reservation
    else:
        return "BAD Request:400"


def computeChar():
    print('START')
    reservation = init()
    reservation = getPrenotated(reservation)
    plt.plot(reservation)
    print('END')
    return 0

def getReservation(users):
    try:
        request = requests.get('http://localhost:60080/reservation/'+users)
    except (Exception):
        return "Error Request:500" 
    if request.status_code == 200: 
        return request.text
    else: 
        return "BAD Request:400"
    
def main_selfbuild():
    reservation = randgen.init()
    randgen.generator()
    reservation = randgen.datapipeline(reservation)
    plt.plot(reservation)
    


if __name__ =='__main__':
    main_selfbuild()