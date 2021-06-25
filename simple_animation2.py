from tkinter import *
import time

gui = Tk()
gui.geometry("800x600")
gui.title("Pi Animation")
canvas = Canvas(gui, width=800,height=600,bg='white')
canvas.pack()

ball1 = canvas.create_oval(7,7,60,60, fill='red')

xa = 5
ya = 10

while True:
 canvas.move(ball1,xa,ya)
 pos=canvas.coords(ball1)
 if pos[3] >=600 or pos[1] <=0:
  ya = -ya
 if pos[2] >=800 or pos[0] <=0:
  xa = -xa
 gui.update()
 time.sleep(.025)

gui.mainloop()