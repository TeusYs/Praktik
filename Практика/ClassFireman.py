from ClassFaier1 import Faier

class Fireman(Faier):

    def __init__(self, canvas, root, time, randint, x, Image, ImageTk, img2, u):
        self.canvas = canvas
        self.root = root
        self.time = time
        self.randint = randint
        self.Image = Image
        self.ImageTk = ImageTk
        self.img2 = img2
        self.u = u
        self.x = x
        super().__init__(canvas, x, Image, ImageTk, img2, randint, u)
    def tsh(self):
        while True:
            def Route2(y):
                    for i in range(self.Movement1[2]):
                        self.canvas.move(self.b, -4, 0)
                        self.root.update()
                        self.time.sleep(0.0005)
                    for i in range(self.Movement1[2]):
                        self.canvas.move(self.b, 0, -4)
                        self.root.update()
                        self.time.sleep(0.0005)
                    self.time.sleep(10)
                    self.canvas.delete(im)
            def Route0(y):
                    for i in range(self.Movement1[7]):
                        self.canvas.move(self.b, -4, 0)
                        self.root.update()
                        self.time.sleep(0.0005)
                    for i in range(self.Movement1[2]):
                        self.canvas.move(self.b, 0, -4)
                        self.root.update()
                        self.time.sleep(0.0005)
                    self.time.sleep(10)
                    self.canvas.delete(im)
            def Route1(y):
                    for i in range(self.Movement1[3]-10):
                        self.canvas.move(self.b, -4, 0)
                        self.root.update()
                        self.time.sleep(0.0005)
                    for i in range(self.Movement1[2]):
                        self.canvas.move(self.b, 0, 4)
                        self.root.update()
                        self.time.sleep(0.0005)
                    self.time.sleep(10)
                    self.canvas.delete(im)
            def Route3(y):
                    for i in range(self.Movement1[1]+23):
                        self.canvas.move(self.b, -4, 0)
                        self.root.update()
                        self.time.sleep(0.0005)
                    for i in range(self.Movement1[2]):
                        self.canvas.move(self.b, 0, 4)
                        self.root.update()
                        self.time.sleep(0.0005)
                    self.time.sleep(10)
                    self.canvas.delete(im)
            def Route4(y):
                    for i in range(self.Movement1[1]+5):
                        self.canvas.move(self.b, 0, -4)
                        self.root.update()
                        self.time.sleep(0.0005)
                    for i in range(self.Movement1[2]+15):
                        self.canvas.move(self.b, 4, 0)
                        self.root.update()
                        self.time.sleep(0.0005)
                    for i in range(self.Movement1[2]+15):
                        self.canvas.move(self.b, 0, -4)
                        self.root.update()
                        self.time.sleep(0.0005)
                    self.time.sleep(10)
                    self.canvas.delete(im)
            def Route5(y):
                    for i in range(self.Movement1[3]):
                        self.canvas.move(self.b, 4, 0)
                        self.root.update()
                        self.time.sleep(0.0005)
                    for i in range(self.Movement1[2]):
                        self.canvas.move(self.b, 0, 4)
                        self.root.update()
                        self.time.sleep(0.0005)
                    self.time.sleep(10)
                    self.canvas.delete(im)
            def Route6(y):
                for i in range(self.Movement1[3]):
                    self.canvas.move(self.b, 4, 0)
                    self.root.update()
                    self.time.sleep(0.0005)
                for i in range(self.Movement1[2]):
                    self.canvas.move(self.b, 0, -4)
                    self.root.update()
                    self.time.sleep(0.0005)
                self.time.sleep(10)
                self.canvas.delete(im)
            self.Movement1 = [204, 112, 45, 95, 75, 222, 142, 199, 370, 320, 52, 33]
            self.color = [['slateblue'], ['green'], ['aqua'], ['blue'], ['plum']]
            self.start = [[1835, 485, 1890, 540], [5, 485, 60, 540], [590, 990, 645, 1045]]
            self.start2 = self.randint(0, 2)
            pilImage = self.Image.open('p.png')
            image = self.ImageTk.PhotoImage(pilImage)
            self.g = self.randint(0, 1)
            y = super().ot2()
            im = super().ot3()
            if self.canvas.coords(im) == [1625.0, 225.0]:
                self.time.sleep(5)
                self.b = self.canvas.create_image(1850, 525, image=image)
                Route2(y)
                self.time.sleep(5)
            elif self.canvas.coords(im) == [1170, 225]:
                self.time.sleep(5)
                self.b = self.canvas.create_image(1850, 525, image=image)
                Route0(y)
                self.time.sleep(5)
            elif self.canvas.coords(im) == [1645, 825]:
                self.time.sleep(5)
                self.b = self.canvas.create_image(1850, 525, image=image)
                Route1(y)
                self.time.sleep(5)
            elif self.canvas.coords(im) == [1185, 825]:
                self.time.sleep(5)
                self.b = self.canvas.create_image(1850, 525, image=image)
                Route3(y)
                self.time.sleep(5)
            elif self.canvas.coords(im) == [710, 225]:
                self.time.sleep(5)
                self.b = self.canvas.create_image(610, 1020, image=image)
                Route4(y)
                self.time.sleep(5)
            elif self.canvas.coords(im) == [255, 825]:
                self.time.sleep(5)
                self.b = self.canvas.create_image(25, 525, image=image)
                Route5(y)
                self.time.sleep(5)
            elif self.canvas.coords(im) == [260, 225]:
                self.time.sleep(5)
                self.b = self.canvas.create_image(25, 525, image=image)
                Route6(y)
                self.time.sleep(5)
