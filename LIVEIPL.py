import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import sys


def scoreboard():
    url = 'https://www.cricbuzz.com/'
    data = requests.get(url).text

    soup = BeautifulSoup(data, 'html.parser')

    teamA = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[0].get_text()
    teamB = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[1].get_text()


    scoreA = soup.find_all(class_='cb-ovr-flo')[8].get_text()
    scoreB = soup.find_all(class_='cb-ovr-flo')[10].get_text()

    return teamA, teamB, scoreA, scoreB


def info():
    global boolean
    team1, team2, score1, score2 = scoreboard()
    teamA.config(text=team1)
    teamB.config(text=team2)
    scoreA.config(text=score1)
    scoreB.config(text=score2)


re = False

#GUI initialization
window = Tk()
icon = r'52740cricketgame_109412.ico'
window.title('LIVE IPL 2020')
window.geometry("700x300")
window.iconbitmap(icon)


team1, team2, score1, score2 = scoreboard()


title = Label(window, text='IPL Season 13 2020', font=('verdana',30,'bold'))
title.place(x = 120, y= 0)

teamA = Label(window, text=team1, font=('serif',15))
teamA.place(x = 100, y= 100)

teamB = Label(window, text=team2, font=('serif',15))
teamB.place(x = 500, y= 100)

scoreA = Label(window, text=score1, font=('serif',15))
scoreA.place(x = 80, y= 150)

scoreB = Label(window, text=score2, font=('serif',15))
scoreB.place(x = 480, y= 150)

refresh = Button(window, text = 'Refresh', command=info)
refresh.place(x=320, y=250)


#player1 image
image = r"{}.png".format(team1.strip())
img = Image.open(image)
img = img.resize((40, 40), Image.ANTIALIAS)

img = ImageTk.PhotoImage(img)
teamA_logo = Label(window, image=img)
teamA_logo.place(x=150, y=90)



#player2 image
image1 = r"{}.png".format(team2.strip())
img1 = Image.open(image1)
img1 = img1.resize((40, 40), Image.ANTIALIAS)

img1 = ImageTk.PhotoImage(img1)
teamA_logo = Label(window, image=img1)
teamA_logo.place(x=550, y=90)


window.mainloop()
sys.exit(1)
