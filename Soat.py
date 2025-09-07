from datetime import datetime
from tkinter import *

ekran = Tk()
ekran.title('Soat')
ekran.geometry('400x400')

soat = Label(bg = 'white')
soat.place(x = 100, y = 100, width = 200, height = 50)
def vaqt() :
	bugun = datetime.today()
	soat.config(text = str(bugun))
time = Button(text= 'Aniq vaqt', command = vaqt)
time.place(x = 120, y = 170, width = 160, height = 40)




ekran.mainloop()
