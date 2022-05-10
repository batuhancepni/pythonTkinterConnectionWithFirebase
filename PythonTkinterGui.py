from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import random
import time

start_time = time.time()


# Fetch the service account key JSON file contents
cred = credentials.Certificate('db-key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://ceo308-relational-db-default-rtdb.europe-west1.firebasedatabase.app/"
})

#ref = db.reference('/new')
#print(ref.get())

#Defining Tkinter
root = Tk()
root.geometry("480x480")
root.title("Read/Write Data App")

entries=[]
entries_values=[]
labels=[]

#Progress Bar
def progressBarPopOp():
    global Getstart_time
    Getstart_time = time.time()
    top5 = Toplevel(root)
    top5.geometry("300x120")
    top5.title("Progress Bar")
    pb = ttk.Progressbar(
        top5,
        orient='horizontal',
        mode='determinate',
        length=280)
    pb.grid(column=0, row=3, columnspan=2, padx=10, pady=20)
    
    for i in range(100):
        pb['value'] = i
        top5.update_idletasks()
        i += 25

    pb.pack()



def getPopOp():
    top2 = Toplevel(root)
    top2.geometry("400x400")
    top2.title("Imported values from Database")
    for i in range(impdata):
        ref = db.reference('/new')
        label1=Label(top2,text=ref.get(), font='time 9 bold').place(x=0,y=20)

def numberOfImportedData():
    global impdata
    impdata=int(e2.get())
    getPopOp()

def pushNewValues():
    ref = db.reference('/new')
    for i in entries:
        k = i.get()
        entries_values.append(k)
        #Write to database
        ref.update({random.randint(100000,999999):k})


def writePopOp():
    top = Toplevel(root)
    top.geometry("400x400")
    top.title("Write the new values")
    Label(top,text='Write your values.', font= "time 13 bold").place(x=50,y=30)
    buttonsp = Button(top,text="Submit",fg="white",bg="green", font="time 13 bold",width=15,command=lambda: [progressBarPopOp(),pushNewValues(),messagebox.showinfo("Info:","Data has been pushed")])
    buttonsp.place(x=15,y=150)
    
    for i in range(wrtdata):
        en = Entry(top)
        en.grid(row=i+1, column=0,sticky=S,pady=2,padx=250)
        entries.append(en)
        
    

def numberOfWritingData():
    global wrtdata
    wrtdata=int(e3.get())
    writePopOp()
    

def getNewWroteDataPopOp():
    top3 = Toplevel(root)
    top3.geometry("400x400")
    top3.title("Imported values from new wrote values.")
    for i in range(wrtdata):
        labels.append(Label(top3,text="Data: "+ entries_values[i]))
        labels[i].place(x=10,y=10+(30*i))


def measureTime():
    processTimeText.set((time.time() - Getstart_time))
        



l1= Label(root,text='Read/Write Data App', font= "time 15 bold")
l1.place(x=30, y=30)



l2= Label(root,text='How many data do you want to get?', font= "time 13 bold")
l2.place(x=30, y=90)

e2 = Entry(root,width = 7, bd=2, font="time 11 bold")
e2.place(x=30,y=120)

button = Button(root,text="Submit",fg="white",bg="green", font="time 13 bold",width=34,command=lambda:[progressBarPopOp(),numberOfImportedData(),measureTime()])
button.place(x=30,y=150)



l3= Label(root,text='How many data do you want to write?', font= "time 13 bold")
l3.place(x=30, y=220)

e3 = Entry(root,width = 7, bd=2, font="time 11 bold")
e3.place(x=30,y=250)

button2 = Button(root,text="Submit",fg="white",bg="green", font="time 13 bold",width=34,command=lambda:[progressBarPopOp(),numberOfWritingData(),measureTime()])
button2.place(x=30,y=280)



l4= Label(root,text='Get the writed data', font= "time 13 bold")
l4.place(x=30, y=350)

button3 = Button(root,text="Submit",fg="white",bg="green", font="time 13 bold",width=34,command=lambda:[progressBarPopOp(),getNewWroteDataPopOp(),measureTime()])
button3.place(x=30,y=380)

#App Start Time
l5= Label(root,text='App Opening Execution Clock:', font= "time 9 bold")
l5.place(x=30, y=430)

entryText = tkinter.IntVar()
timeEntry = tkinter.Entry(root, textvariable=entryText, state='disabled')
timeEntry.place(x=210,y=430)

#Processing Times (Clicking Button, Read/Write Data)
l6= Label(root,text='Process Time Clock:', font= "time 9 bold")
l6.place(x=30, y=460)

processTimeText = tkinter.IntVar()
processTimeEntry = tkinter.Entry(root, textvariable=processTimeText, state='disabled')
processTimeEntry.place(x=160,y=460)




entryText.set((time.time() - start_time))
root.mainloop()
