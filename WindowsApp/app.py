from tkinter import *
import random # For random functions
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyodbc
import json
import numpy as np
import schedule
import time

conn = pyodbc.connect('DSN=TallyODBC64_9000;SERVER=({local});DRIVER=Tally ODBC DRIVER64;PORT=9000')

cursor=conn.cursor()

data=cursor.execute("SELECT $Name FROM Company")

columns = [column[0] for column in data.description]
actual_cols=[s.strip('$') for s in columns]
rows = data.fetchall()

cred = credentials.Certificate('C:/Users/patel/Documents/python/WindowsApp/agro-servicecenter-firebase-adminsdk-zikwb-f3b24f9228.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

running = False





def scanning():
    if running:  # Only do this if the Stop button has not been clicked
        print("hello")
        MyRandom = random.randint(1,6)
        dice_thrown.configure(text="Dice thrown: " + str(MyRandom))

    # After 1 second, call scanning again (create a recursive loop)
    root.after(1000, scanning)

def start():
    """Enable scanning by setting the global flag to True."""
    
    global running
    running = True

def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False
    
    

def job():
    users_ref = db.collection(u'CustomerData')
    docs = users_ref.stream()

    doc_ref = db.collection(u'users').document(u'Query')
    doc_ref.set({
        u'Query': str(rows)
    })


        
root = Tk()
 
root.title('Agro Service Centre')
root.iconbitmap(r"agro.ico")



app = Frame(root)
app.grid()

MyTitle = Label(app, text="Sync Data",font="Helvetica 16 bold")
MyTitle.grid()
 
start = Button(app, text="Start Sync", command=job)


stop = Button(app, text="Stop Sync", command=stop)

 
dice_thrown = Label(app, font="Helvetica 16 bold")
dice_thrown.grid()

start.grid()
stop.grid()

root.after(1000, scanning)

root.mainloop()

