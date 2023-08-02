from tkinter import *

class Example(Frame):
    def __init__(self, parent, yukseklik, genislik):
        Frame.__init__(self, parent)
        self.parent = parent
        self.yukseklik = yukseklik
        self.genislik = genislik
        self.InitGui()

    def InitGui(self):
        self.pack()
        self.canvas = Canvas(self)
        self.canvas.pack()

    def bar_diagram(self, app):
        self.pack()

        self.cnvsrect1 = self.canvas.create_rectangle(0, 600, 75, 300 - (app[0]*3), fill="red")
        self.cnvsrect2 = self.canvas.create_rectangle(80, 600, 150, 300 - (app[1]*3), fill="red")
        self.cnvsrect3 = self.canvas.create_rectangle(155, 600, 225, 300 - (app[2]*3), fill="red")
        self.cnvsrect4 = self.canvas.create_rectangle(230, 600, 300, 300 - (app[3]*3), fill="red")
        self.cnvsrect5 = self.canvas.create_rectangle(305, 600, 375, 300 - (app[4]*3), fill="red")

        self.cnvstxt1 = self.canvas.create_text(40, 250, text=app[0], fill="red")
        self.cnvstxt2 = self.canvas.create_text(115, 250, text=app[1], fill="red")
        self.cnvstxt3 = self.canvas.create_text(190, 250, text=app[2], fill="red")
        self.cnvstxt4 = self.canvas.create_text(265, 250, text=app[3], fill="red")
        self.cnvstxt5 = self.canvas.create_text(340, 250, text=app[4], fill="red")

        self.canvas.tag_bind(self.cnvsrect1, "<Button-1>", self.mouse_tikla1)
        self.canvas.tag_bind(self.cnvsrect1, "<ButtonRelease-1>", self.mouse_birak1)
        self.canvas.tag_bind(self.cnvsrect2, "<Button-1>", self.mouse_tikla2)
        self.canvas.tag_bind(self.cnvsrect2, "<ButtonRelease-1>", self.mouse_birak2)
        self.canvas.tag_bind(self.cnvsrect3, "<Button-1>", self.mouse_tikla3)
        self.canvas.tag_bind(self.cnvsrect3, "<ButtonRelease-1>", self.mouse_birak3)
        self.canvas.tag_bind(self.cnvsrect4, "<Button-1>", self.mouse_tikla4)
        self.canvas.tag_bind(self.cnvsrect4, "<ButtonRelease-1>", self.mouse_birak4)
        self.canvas.tag_bind(self.cnvsrect5, "<Button-1>", self.mouse_tikla5)
        self.canvas.tag_bind(self.cnvsrect5, "<ButtonRelease-1>", self.mouse_birak5)

        self.canvas.bind("<Enter>", self.mouse_uzerinde1)
        self.canvas.bind("<Leave>", self.mouse_uzerinde_degil1)

        self.canvas.pack()

    def mouse_uzerinde1(self, event):
        if self.canvas.itemcget(self.cnvstxt1, "fill") == "red":
            self.canvas.itemconfig(self.cnvstxt1, fill="white")
        else:
            self.canvas.itemconfig(self.cnvstxt1, fill="red")

        if self.canvas.itemcget(self.cnvstxt2, "fill") == "red":
            self.canvas.itemconfig(self.cnvstxt2, fill="white")
        else:
            self.canvas.itemconfig(self.cnvstxt2, fill="red")

        if self.canvas.itemcget(self.cnvstxt3, "fill") == "red":
            self.canvas.itemconfig(self.cnvstxt3, fill="white")
        else:
            self.canvas.itemconfig(self.cnvstxt3, fill="red")

        if self.canvas.itemcget(self.cnvstxt4, "fill") == "red":
            self.canvas.itemconfig(self.cnvstxt4, fill="white")
        else:
            self.canvas.itemconfig(self.cnvstxt4, fill="red")

        if self.canvas.itemcget(self.cnvstxt5, "fill") == "red":
            self.canvas.itemconfig(self.cnvstxt5, fill="white")
        else:
            self.canvas.itemconfig(self.cnvstxt5, fill="red")

    def mouse_uzerinde_degil1(self, event):
        self.canvas.itemconfig(self.cnvstxt1, fill="red")
        self.canvas.itemconfig(self.cnvstxt2, fill="red")
        self.canvas.itemconfig(self.cnvstxt3, fill="red")
        self.canvas.itemconfig(self.cnvstxt4, fill="red")
        self.canvas.itemconfig(self.cnvstxt5, fill="red")

    def mouse_tikla1(self, event):
        if self.canvas.itemcget(self.cnvsrect1, "fill") == "red":
            self.canvas.itemconfig(self.cnvsrect1, fill="blue")
        else:
            self.canvas.itemconfig(self.cnvsrect1, fill="red")

    def mouse_birak1(self, event):
        self.canvas.itemconfig(self.cnvsrect1, fill="red")

    def mouse_tikla2(self, event):
        if self.canvas.itemcget(self.cnvsrect2, "fill") == "red":
            self.canvas.itemconfig(self.cnvsrect2, fill="blue")
        else:
            self.canvas.itemconfig(self.cnvsrect2, fill="red")

    def mouse_birak2(self, event):
        self.canvas.itemconfig(self.cnvsrect2, fill="red")

    def mouse_tikla3(self, event):
        if self.canvas.itemcget(self.cnvsrect3, "fill") == "red":
            self.canvas.itemconfig(self.cnvsrect3, fill="blue")
        else:
            self.canvas.itemconfig(self.cnvsrect3, fill="red")

    def mouse_birak3(self, event):
        self.canvas.itemconfig(self.cnvsrect3, fill="red")

    def mouse_tikla4(self, event):
        if self.canvas.itemcget(self.cnvsrect4, "fill") == "red":
            self.canvas.itemconfig(self.cnvsrect4, fill="blue")
        else:
            self.canvas.itemconfig(self.cnvsrect4, fill="red")

    def mouse_birak4(self, event):
        self.canvas.itemconfig(self.cnvsrect4, fill="red")

    def mouse_tikla5(self, event):
        if self.canvas.itemcget(self.cnvsrect5, "fill") == "red":
            self.canvas.itemconfig(self.cnvsrect5, fill="blue")
        else:
            self.canvas.itemconfig(self.cnvsrect5, fill="red")

    def mouse_birak5(self, event):
        self.canvas.itemconfig(self.cnvsrect5, fill="red")


def test_fonksiyonu():

    root = Tk()
    root.title("Goruntu Ekrani")
    ekran_boyutlari = [600, 400]
    root.geometry("{}x{}".format(ekran_boyutlari[0], ekran_boyutlari[1]))
    app = Example(root, ekran_boyutlari[0], ekran_boyutlari[1])
    app.bar_diagram([100, 90, 70, 60, 100])

    root.mainloop()


test_fonksiyonu()