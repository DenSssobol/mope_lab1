from random import *
from tkinter.filedialog import *

class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("Лабораторна робота №1")
        self.root.geometry("700x800")
        self.root.configure(background="#8cb6da")
        self.leb_autor = Label(self.root, text="Соболь Д.Д.\nIO-92\n Вариант №18",font=("Times New Roman", 20),justify=CENTER,bg="#8cb6da")
        self.leb_autor.place(x=250,y=25)
        self.root.resizable(False, False)

        self.a0 = randint(0, 20)
        self.a1 = randint(0, 20)
        self.a2 = randint(0, 20)
        self.a3 = randint(0, 20)

        self.X1 = []
        self.X2 = []
        self.X3 = []

        for i in range(0, 8):
            self.X1.append(randint(0, 20))
            self.X2.append(randint(0, 20))
            self.X3.append(randint(0, 20))

        self.Y=[]

        for i in range(0, 8):
            self.Y.append(self.a0 + self.a1 * self.X1[i] + self.a2 * self.X2[i] + self.a3 * self.X3[i])

        self.X0 = [((max(self.X1) + min(self.X1)) / 2), ((max(self.X2) + min(self.X2)) / 2), ((max(self.X3) + min(self.X3)) / 2)]
        self.dx = [(max(self.X1) - self.X0[0]), (max(self.X2) - self.X0[1]), (max(self.X3) - self.X0[2])]

        self.XN1 = []
        self.XN2 = []
        self.XN3 = []

        for i in range(0, 8):
            self.XN1.append(round((self.X1[i] - self.X0[0]) / self.dx[0], 1))
            self.XN2.append(round((self.X1[i] - self.X0[1]) / self.dx[1], 1))
            self.XN3.append(round((self.X1[i] - self.X0[2]) / self.dx[2], 1))

        self.Yet = self.a0 + self.a1 * self.X0[0] + self.a2 * self.X0[1] + self.a3 * self.X0[2]

        self.MAXY = max(self.Y)
        self.IND_MAX_y = self.Y.index(self.MAXY)
        self.tp = [self.X1[self.IND_MAX_y], self.X2[self.IND_MAX_y], self.X3[self.IND_MAX_y]]
        self.fkv = self.a0 + self.a1 * self.X1[self.IND_MAX_y] + self.a2 * self.X2[self.IND_MAX_y] + self.a3 * self.X3[self.IND_MAX_y]

        self.lab_names = Label(self.root, text="№    X1     X2     X3       Y         XN1    XN2    XN3",font=("Times New Roman", 17),justify=CENTER,bg="#8cb6da")
        self.lab_names.place(x=80,y=140)

        self.xi=80
        self.yi=180

        for i in range(8):
            self.text_i=str(i+1)+"  |  "+str(self.X1[i])+"  |   "+str(self.X2[i])+"   |   " +str(self.X3[i])+"   |  |  " +str(self.Y[i])+ "   |  |   "+ str(self.XN1[i])+"   |  "+ str(self.XN2[i])+"  |   "+str(self.XN3[i])
            self.lab_i=Label(self.root, text=self.text_i,font=("Times New Roman", 17),justify=CENTER,bg="#8cb6da")
            self.lab_i.place(x=self.xi,y=self.yi+i*40)

        self.text_x0 = "X0 |" + str(self.X0[0]) + " | " + str(self.X0[1]) + " | " + str(self.X0[2]) + " |  | " + str(self.Yet) + " |  |                    "
        self.lab_x0 = Label(self.root, text=self.text_x0,font=("Times New Roman", 17), justify=CENTER, bg="#8cb6da")
        self.lab_x0.place(x=70, y=500)

        self.text_dx = "dx  |" + str(self.dx[0]) + "  |" + str(self.dx[1]) + "  | " + str(self.dx[2]) + " |  |                                    "
        self.lab_dx = Label(self.root, text=self.text_dx, font=("Times New Roman", 17), justify=CENTER, bg="#8cb6da")
        self.lab_dx.place(x=70, y=540)

        self.text_a ="a0 = "+str(self.a0)+", a1 = "+str(self.a1)+", a2 = "+str(self.a2)+", a3 = "+str(self.a3)
        self.lab_a = Label(self.root, text=self.text_a, font=("Times New Roman", 17), justify=CENTER, bg="#8cb6da")
        self.lab_a.place(x=80, y=620)

        self.text_y1 = "Y = " + str(self.a0) + " + " + str(self.a1) + "*X1" +"+" + str(self.a2) + "*X2" + "+" + str(self.a3) + "*X3"
        self.lab_y1 = Label(self.root, text=self.text_y1, font=("Times New Roman", 17), justify=CENTER, bg="#8cb6da")
        self.lab_y1.place(x=80, y=660)

        self.text_y2 = "Yет = " + str(self.a0) + " + " + str(self.a1) + "*" + str(self.X0[0]) + "+" + str(self.a2) + "*" + str(self.X0[1]) + "+" + str(self.a3) + "*" + str(self.X0[2]) + " = " + str(self.Yet)
        self.lab_y2 = Label(self.root, text=self.text_y2, font=("Times New Roman", 17), justify=CENTER, bg="#8cb6da")
        self.lab_y2.place(x=80, y=700)

        self.text_OTP = "MAX(Y) = " + str(self.MAXY) + " = Y(" + str(self.tp[0]) + ", " + str(self.tp[1]) + ", " + str(self.tp[2]) + ")"
        self.lab_OTP = Label(self.root, text=self.text_OTP, font=("Times New Roman", 17), justify=CENTER, bg="#8cb6da")
        self.lab_OTP.place(x=80, y=740)

        self.root.mainloop()


def main():
    print("Моя група: ІО-92\nМій варіант: 18")
    Window()

if __name__ == "__main__":
    main()