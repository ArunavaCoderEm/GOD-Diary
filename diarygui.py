# Library

import datetime
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import speech_recognition as sr

# splash screen

splash = Tk()
splash.title ('GOD-Diary')
splash.geometry ('400x400')
splash.resizable (0,0)
splash.configure (background = 'red')
spl_lab = Label (splash, text = 'GodARD Devos \n GOD-Diary', bg = 'yellow', fg = 'blue', font = ('vendana', 20, 'bold'))
spl_lab.pack (pady = 150)

# Main window

def main_window():
    
    splash.destroy()
       
    rootGOD = tk.Tk()
    rootGOD.geometry ('600x300')
    rootGOD.title('GOD-Diary')
    rootGOD.resizable (0,0)
    rootGOD.minsize (width = 950, height = 500)
    rootGOD.configure(background="green")

    label = Label(rootGOD,text="- Your Name - ", fg='blue',font=('vendana',15,'bold'))
    label.pack()
    
    nameA = Entry(rootGOD, width=25, bg="aqua",fg="black",font=('vendana',25,'bold'))
    nameA.pack()
    
    def create_directory():
        current_date = datetime.date.today()
        directory_name = current_date.strftime('%Y-%m-%d')
        if not os.path.exists(directory_name):
            os.mkdir(directory_name)
            
    def save_entry():
        create_directory()
        current_date_time = datetime.datetime.now()
        file_name = current_date_time.strftime('%Y-%m-%d %H-%M-%S')
        entry = text_entry.get('1.0', 'end-1c')
        directory_name = current_date_time.strftime('%Y-%m-%d')
        file_path = os.path.join(directory_name, file_name + '.txt')
        with open(file_path, 'w') as file:
            file.write(entry)
        messagebox.showinfo ( 'GOD-Diary', 'Saved \n Successfully ! ')

    def quitt():
        messagebox.showinfo ( 'GOD-Diary', 'You Want To Exit ? \n Done Describing Your Day ? ')
        return rootGOD.destroy()

    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
            query = r.recognize_google(audio, language = "en-in")
            text_entry.insert(tk.END, query)
            
    def clear2():
        text_entry.delete("1.0","end")


    labela = Label(rootGOD,text="- YOUR CONTENT EITHER WRITE OR SPEAK -", fg='blue',font=('vendana',15,'bold'))
    labela.pack()

    text_entry = tk.Text(rootGOD, height=20, width=500, bg="pink",fg="black",font=('vendana',10,'bold'))
    text_entry.pack()

    save_button = tk.Button(rootGOD, text='Save', command= save_entry,width=10,height=2,bg="aqua",fg="blue",font=("vendana",12,"bold"))
    save_button.place(x= 110,y=450)

    saytorecord = tk.Button(rootGOD, text='Tell Me', command= listen,width=10,height=2,bg="aqua",fg="blue",font=("vendana",12,"bold"))
    saytorecord.place(x= 220,y=450)

    clear2 = tk.Button(rootGOD, text='Clear', command= clear2,width=10,height=2,bg="aqua",fg="blue",font=("vendana",12,"bold"))
    clear2.place(x= 330,y=450)

    quit_button = tk.Button(rootGOD, text='Quit', command= quitt,width=10,height=2,bg="aqua",fg="blue",font=("vendana",12,"bold"))
    quit_button.place(x= 440,y=450)


# spalsh screen timer

splash.after ( 2500, main_window)

# run app

mainloop()