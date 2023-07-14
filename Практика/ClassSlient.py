from ClassFaier1 import Faier

class Client(Faier):

    def __init__(self, canvas, root, time, randint, x, Image, ImageTk, img2, u):
        self.canvas = canvas
        self.root = root
        self.time = time
        self.randint = randint
        self.Image = Image
        self.ImageTk = ImageTk
        self.img2 = img2
        self.x = x
        super().__init__(canvas, x, Image, ImageTk, img2, randint, u)

    def oval(self):
        def Route0(y):
            for i in range(self.Movement2[0]):
                self.canvas.move(self.b, 2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[10]):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[1]+12):
                    self.canvas.move(self.b, 0, 4)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]):
                self.canvas.move(self.b, 0, 2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[1]):
                    self.canvas.move(self.b, 0, -4)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[10]):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[1]+12):
                    self.canvas.move(self.b, 0, 4)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]):
                self.canvas.move(self.b, 0, -2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[10]):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[1] + 12):
                    self.canvas.move(self.b, 0, 4)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[0]):
                self.canvas.move(self.b, 2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[2]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]):
                self.canvas.move(self.b, 0, -2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]):
                self.canvas.move(self.b, 0, 2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[2]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[2]):
                self.canvas.move(self.b, 2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            self.canvas.delete(self.b)
        def Route1(y):
            for i in range(self.Movement2[3]):
                self.canvas.move(self.b, 2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[3]):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[4]):
                self.canvas.move(self.b, 0, -2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[4]):
                    self.canvas.move(self.b, 0, 4)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[3]):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[4]):
                self.canvas.move(self.b, -2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                self.canvas.delete(self.b)
            for i in range(self.Movement2[4]):
                self.canvas.move(self.b, 2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                self.canvas.delete(self.b)
            for i in range(self.Movement2[4]):
                self.canvas.move(self.b, 0, 2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[3]):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[5]):
                self.canvas.move(self.b, 2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[6]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[3]):
                self.canvas.move(self.b, 0, 2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[3]):
                    self.canvas.move(self.b, 0, -4)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[6]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[3]):
                self.canvas.move(self.b, 0, -2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[6]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[6]):
                self.canvas.move(self.b, 2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            self.canvas.delete(self.b)
        def Route2(y):
            for i in range(self.Movement2[7]):
                self.canvas.move(self.b, -2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[7]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]):
                self.canvas.move(self.b, 0, -2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[1]):
                    self.canvas.move(self.b, 0, 4)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[7]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[2]):
                self.canvas.move(self.b, 2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[2]):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[1]):
                    self.canvas.move(self.b, 0, 4)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[7]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[2]):
                self.canvas.move(self.b, 0, 2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[2]):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[4]):
                    self.canvas.move(self.b, 0, 4)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[7]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[2]):
                self.canvas.move(self.b, -2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[4]):
                    self.canvas.move(self.b, 0, 4)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[7]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[4]):
                self.canvas.move(self.b, 0, 2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[7]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]):
                self.canvas.move(self.b, -2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[1]):
                    self.canvas.move(self.b, 0, 4)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]):
                self.canvas.move(self.b, 0, 2)
                self.root.update()
                self.time.sleep(0.0005)
            self.canvas.delete(self.b)
        def Route3(y):
            for i in range(self.Movement2[8]):
                self.canvas.move(self.b, -2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[3]):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]):
                self.canvas.move(self.b, 0, 2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[1]):
                    self.canvas.move(self.b, 0, -4)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[3]):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]):
                self.canvas.move(self.b, 0, -2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[3]):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[9]):
                self.canvas.move(self.b, 2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[2]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]):
                self.canvas.move(self.b, 0, -2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]):
                self.canvas.move(self.b, 0, 2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[2]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[10]):
                self.canvas.move(self.b, 2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            self.canvas.delete(self.b)
        def Route4(y):
            for i in range(self.Movement2[1]+8):
                self.canvas.move(self.b, 0, -2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[1]+30):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[9]):
                self.canvas.move(self.b, 2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            self.canvas.delete(self.b)
        def Route5(y):
            for i in range(self.Movement2[1]+8):
                self.canvas.move(self.b, 0, -2)
                self.root.update()
                self.time.sleep(0.0005)
            options = self.canvas.itemconfig(y)
            if options['fill'][4] == 'red':
                for i in range(self.Movement1[1] + 30):
                    self.canvas.move(self.b, -4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.canvas.delete(self.b)
            for i in range(self.Movement2[1]+60):
                self.canvas.move(self.b, -2, 0)
                self.root.update()
                self.time.sleep(0.0005)
            self.canvas.delete(self.b)
        while True:
            self.Movement2 = [408, 225, 100, 190, 150, 445, 285, 397, 740, 640, 105]
            self.Movement1 = [204, 112, 50, 95, 75, 222, 142, 199, 370, 320, 52]
            self.color = [['slateblue'], ['green'], ['aqua'], ['blue'], ['plum']]
            self.start = [[1835, 485, 1890, 540], [5, 485, 60, 540], [590, 990, 645, 1045]]
            self.start2 = self.randint(0, 2)
            pilImage = self.Image.open('v2.png')
            pilImage1 = self.Image.open('v1.png')
            pilImage2 = self.Image.open('v3.png')
            pilImage3 = self.Image.open('v4.PNG')
            pilImage4 = self.Image.open('v5.png')
            pilImage5 = self.Image.open('v6.png')
            p = []
            p.append(pilImage)
            p.append(pilImage1)
            p.append(pilImage2)
            p.append(pilImage3)
            p.append(pilImage4)
            p.append(pilImage5)
            image = self.ImageTk.PhotoImage(p[self.randint(0, 5)])
            if self.start2 == 0:
                self.time.sleep(self.randint(0, 10))
                self.b = self.canvas.create_image(1850, 525, image=image)
            elif self.start2 == 1:
                self.time.sleep(self.randint(0, 10))
                self.b = self.canvas.create_image(25, 525, image=image)
            elif self.start2 == 2:
                self.time.sleep(self.randint(0, 10))
                self.b = self.canvas.create_image(610, 1020, image=image)
            self.g = self.randint(0, 1)
            y = super().ot2()
            if self.start2 == 1:
                if self.g == 0:
                    Route0(y)
                else:
                    Route1(y)
            elif self.start2 == 0:
                if self.g == 0:
                    Route2(y)
                else:
                    Route3(y)
            elif self.start2 == 2:
                if self.g == 0:
                    Route4(y)
                else:
                    Route5(y)
            self.time.sleep(self.randint(1, 5))
            options = self.canvas.itemconfig(super().ot2())
            if options['fill'][4] == 'red':
                break