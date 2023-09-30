import plot as plt
import requests

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

def datapipeline(reservation,filenames):
    for filename in filenames : 
        try:
            fin = open(filename, 'rt')
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
    request = requests.get('http://localhost:60080/lezioni')
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

def getPrenotated(reservation):
    request = requests.get('http://localhost:60080/reservation')
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
        return(reservation)


def computeChar():
    print('START')
    reservation = init()
    reservation = getPrenotated(reservation)
    plt.plot(reservation)
    print('END')
    return 0

def getReservation(users):
    request = requests.get('http://localhost:60080/reservation/'+users)
    if request.status_code == 200: 
        return request.text

if __name__ =='__main__':
    computeChar()