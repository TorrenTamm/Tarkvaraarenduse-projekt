from tkinter import *  # Importib tkinter mooduli


# Peamine funktsioon
def run():
    name1 = name_storage.get()  # Saab nimevarust nime
    print(name1)  # Kuvab selle nime konsoolis
    name.delete(0, END)  # Kustutab selle nime, et kast tühjeneks


screen = Tk()  # Loob Tk objekti
screen.title("Minu esimene graafiline programm")  # Seab ekraani
screen.geometry("500x500")  # Seab ekraani suuruse

welcome_text = Label(text="Welcome to our first graphics program ", fg="red", bg="yellow")  # Seab tervitusteksti
welcome_text.pack()  # Pakib teksti plokki,et paremini paigutada

click_me = Button(text="Vajuta mind", fg="red", bg="yellow", command=run)  # Teeb "vajuta mind" nupu
click_me.place(x=10, y=20)  # Paigutab selle nupu

name_storage = StringVar()  # Loob nimevaru
name = Entry(textvariable=name_storage)  # Loob kasti, kuhu saab kirjutada
name.pack()  # Pakib selle kasti plokki, et paremini paigutada
screen.mainloop()  # Paneb koodi igavesti jooksma, et ekraan säiliks
