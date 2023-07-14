class Faier():

    def __init__(self, canvas, x, Image, ImageTk, im2, randint, u):
        self.canvas = canvas
        self.Image = Image
        self.ImageTk = ImageTk
        self.im2 = im2
        self.im2 = im2
        self.randint = randint

    def ot2(self):
        return self.x

    def ot3(self):
        return self.u

    def faier1(self, kor):
        r = [[1625, 225], [1170, 225], [710, 225], [260, 225], [255, 825], [1185, 825], [1645, 825]]
        r1 = r[self.randint(0, 6)]
        self.canvas.coords(kor, r1[0], r1[1])
