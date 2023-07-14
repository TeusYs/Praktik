from tkinter import *
from PIL import Image, ImageTk

import time
from random import randint
from threading import Thread
from ClassFaier1 import Faier
from ClassFireman import Fireman
from ClassSlient import Client

def ot(event):
    canvas.itemconfig(x, fill='red')
    f.faier1(z)
    # p1.tsh(z)
    # Thread(target=p1.tsh(z)).start()
root = Tk()
root.geometry('1900x1080')
#root.attributes('-fullscreen', True)
canvas = Canvas(root, width=1979, height=1079)
canvas.focus_set()
canvas.pack()

pilImage = Image.open("amp_2.jpg")
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(950, 520, image=image)

x = canvas.create_oval(60, 60, 120, 120, fill="yellow")

pilImage2 = Image.open('faier.png')
image2 = ImageTk.PhotoImage(pilImage2)

z = canvas.create_image(-1000, 0, image=image2)
print(canvas.coords(z))

f = Faier(canvas, x, Image, ImageTk, image2, randint, z)
p1 = Fireman(canvas, root, time, randint, x, Image, ImageTk, image2, z)

canvas.tag_bind(x, '<ButtonPress-1>', ot)

c1 = Client(canvas, root, time, randint, x, Image, ImageTk, image2, z)
c2 = Client(canvas, root, time, randint, x, Image, ImageTk, image2, z)
c3 = Client(canvas, root, time, randint, x, Image, ImageTk, image2, z)
c4 = Client(canvas, root, time, randint, x, Image, ImageTk, image2, z)
c5 = Client(canvas, root, time, randint, x, Image, ImageTk, image2, z)
c6 = Client(canvas, root, time, randint, x, Image, ImageTk, image2, z)
c7 = Client(canvas, root, time, randint, x, Image, ImageTk, image2, z)
c8 = Client(canvas, root, time, randint, x, Image, ImageTk, image2, z)

Thread(target=c1.oval).start()
Thread(target=c2.oval).start()
Thread(target=c3.oval).start()
Thread(target=c4.oval).start()
Thread(target=c5.oval).start()
Thread(target=c6.oval).start()
Thread(target=c7.oval).start()
Thread(target=c8.oval).start()
Thread(target=p1.tsh).start()

button = Button(root, text="Выход", command=root.destroy)
canvas_widget = canvas.create_window(25, 1066, window=button)

root.mainloop()