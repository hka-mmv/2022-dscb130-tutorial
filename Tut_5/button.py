#from bs4 import BeautifulSoup
import requests
from datetime import date
from tkinter import *
import tkinter

# ID Vorschläge
def ID():
        myLabel1 = Label(root, text='1: Mensa Am Adenauerring')
        myLabel1.grid(row=3)
        myLabel2 = Label(root, text='2: Mensa Moltkestraße')
        myLabel2.grid(row=4)
        myLabel3 = Label(root, text='3: Mensa Erzbergerstraße')
        myLabel3.grid(row=5)
        myLabel4 = Label(root, text='4: Mensa Schloss Gottesaue')
        myLabel4.grid(row=6)
        myLabel5 = Label(root, text='5: Mensa Tiefenbronner Straße')
        myLabel5.grid(row=7)
        myLabel6 = Label(root, text='6: Mensa Holzgartenstraße')
        myLabel6.grid(row=8)

# API Abfrage
def abfrage():


        id = entry.get()

        datum = date.today()

        URL = f"https://www.iwi.h-ka.de/iwii/REST/canteen/v2/{id}/{datum}"
        data = requests.get(URL).json()

        anzahl_gerichte = len(data['mealGroups'])

        if anzahl_gerichte != 0:
                for i in range(anzahl_gerichte):
                        Label(root, text=data['mealGroups'][i]['title'], font=('Helvetica', 12, 'bold')).grid()
                        Label(root, text=data['mealGroups'][i]['meals'][0]['name']).grid()
                        if data['mealGroups'][i]['title'] == 'Gut und Günstig':
                                Label(root, text=data['mealGroups'][i]['meals'][1]['name'],fg='green').grid()
        else:
                Label(root, text=data['status'] + ', see you on monday!').grid(row=14) 
        

# creating the window
root = Tk()
root.geometry('400x600') 
root.title("Mensagerichte")

# defining input box
entry = Entry(root)
entry.grid(row=9)
entry.insert(0, "Gebe eine ID ein")

# defining a button for IDs
myButton1 = Button(root, text='Mensa-ID\'s', command=ID, padx = 50, pady = 25)
myButton1.grid(row=1)

# defining button for API call 
myButton2 = Button(root, text='Was gibt es heute?', command=abfrage, padx = 50, pady = 25)
myButton2.grid(row=10)


# refresh loop 
root.mainloop()





