from tkinter import Tk  # impordib tkinteri Tk
from tkinter import Label  # impordib tkinteri Label'i
import time  # impordib time mooduli

master = Tk()  # Defineerib master'i
master.title("Digital Clock")  # Seadistab masteri tiitli


# Aja functsioon
def get_time():
    timeVar = time.strftime("%I:%M:%S %p")  # Konverdib kellaaja antud formaati
    clock.config(text=timeVar)  # Seadistab tekstiks aja
    clock.after(200, get_time)  # Käivitab funktsiooni uuesti 200 ms pärast


Label(master,font=("Arial",30),text="Digital Clock",fg="white",bg="black").pack()  # Seadistab teksti ja formaadi
clock = Label(master, font=("Arial",100),bg="black",fg="white")  # Seadistab aja teksti
clock.pack()  # Pakkib kella figuuri, et seda paigutada

get_time()  # Käivitab funktsiooni

master.mainloop()  # Paneb koodi kordusesse
