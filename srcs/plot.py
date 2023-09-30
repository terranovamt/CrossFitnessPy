import matplotlib.pyplot as plt
import datetime

def plot(reservation):
    
    x={}
    y={}
    for day in reservation:
        xday = []
        yday = []
        lessons = reservation[day]
        for lesson in lessons:
            xday.append(list(lesson.values())[0]+"\nore: "+str(list(lesson.keys())[0])+":00")
            yday.append(lesson["counter"])

        x[day] = xday
        y[day] = yday

    fig, ax = plt.subplots(3, 2,figsize=(12,8))

    ax[0][0].set_title('Lunedì')
    # ax[0][0].set_xlabel('LEZIONI')
    ax[1][0].set_title('Martedì')
    # ax[1][0].set_xlabel('LEZIONI')
    ax[2][0].set_title('Mercoledì')
    # ax[2][0].set_xlabel('LEZIONI')
    ax[0][1].set_title('Giovedì')
    # ax[0][1].set_xlabel('LEZIONI')
    ax[1][1].set_title('Venerdì')
    # ax[1][1].set_xlabel('LEZIONI')
    fig.delaxes(ax[2][1])

    list_ax=[ax[0][0],ax[1][0],ax[2][0],ax[0][1],ax[1][1],ax[2][1]]
    
    c = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
   
    for key in x:
        list_ax[key-1].bar(x[key], y[key])#, color = c[0:len(x[key])])
        list_ax[key-1].plot(x[key], y[key],color="red")
        list_ax[key-1].scatter(x[key], y[key])
        list_ax[key-1].tick_params(axis="x", labelsize=6)

    plt.subplots_adjust(left=0.125,
                        bottom=0.1, 
                        right=0.9, 
                        top=0.9, 
                        wspace=0.2, 
                        hspace=0.5)
    # plt.savefig("test.png")
    plt.show()