import matplotlib.pyplot as plt
import requests
from tkinter import filedialog as fd


def plot(reservation):
    
    fig, ax = plt.subplots()

    lesson = ['Acro Yoga','Functional','Crossfit','Yoga' ]
    counts = [1,0,2,0]
    # bar_labels = ['red']
    # bar_colors = ['tab:red']

    # ax.bar(lesson, counts, label=bar_labels, color=bar_colors)

    # ax.set_ylabel('fruit supply')
    # ax.set_title('Fruit supply by kind and color')
    # ax.legend(title='Fruit color')

    # plt.show()

    # lesson = ['apple', 'blueberry', 'cherry', 'orange']
    # counts = [40, 100, 30, 55]
    bar_labels = ['red', 'blue', 'green', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

    ax.bar(lesson, counts, label=bar_labels, color=bar_colors)
    ax.scatter(lesson, counts)

    ax.plot(lesson, counts)

    ax.set_xlabel('Lunedì')
    ax.set_title('LEZIONI')

    plt.show()

def files():
  filenames =  fd.askopenfilenames(filetypes=[('Memebr','*.txt')])
  return filenames

def datapipeline(reservation,filenames):


    for filename in filenames : 
        try:
            fin = open(filename, 'rt')
        except FileNotFoundError:
            print('>>> FileNotFound ERROR: check path or exension of file')


        member_name = filename.split('/')[9][:-4]
        print(member_name)
        for line in fin:
            words=line[:-1].split('|')
            in_lesson = words[0]
            day=int(words[1][0:1])
            hour=int(words[1][1:3])
            for lesson in reservation[day]:
                try:
                    if lesson[hour] == in_lesson:
                        lesson['counter'] = lesson['counter'] + 1
                        break
                except Exception:
                    pass
        return(reservation)


def init():
    # request = requests.get('http://example.com/foo/bar')
    # print(request.status_code)
    # print(request.headers)
    # print(request.content)  # bytes
    # print(request.text)     # r.c``ontent as str
    # reservation = dict(request.text)
    reservation ={
        1 : [
            {8 : 'Yoga', 'counter' : 0},
            {10 : 'Crossfit', 'counter' : 0}
             ],
        2 : [
            {10 : 'Yoga', 'counter' : 0},
            {16 : 'Crossfit Class', 'counter' : 0}
             ],
        3 : [
            {14 : 'Yoga', 'counter' : 0}
             ],
        5 : [
            {16 : 'Crossfit Class', 'counter' : 0}
            ]
    }
    print(reservation.keys())
    print(type(list(reservation.keys())[2]))
    return reservation



def main():
    reservation = init()
    table = files()
    reservation = datapipeline(reservation,table)
    plot(reservation)
    print('END')
    return 0

if __name__ =='__main__':
    main()