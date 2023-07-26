import tkinter


global Bild

# bisheriger Aufbau mit Knopf, Fläche und Bild
class simpleapp_tk(tkinter.Tk):
    
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        global Bild

        # frame erstellen, mit fester Höhe und Breite
        self.frameWuerfel = tkinter.Frame(self, bg='#FBD975', height = 200, width = 200)
        self.frameWuerfel.place(x=0, y=0)

        #Knopf erstellen mit festem Platz als xy-Koordinate und fester Höhe und Breite
        self.button1 = tkinter.Button(self,text="klick",command=self.OnButtonEinsClick)
        self.button1.place(x=65, y=160, width=70, height=40)
        
        #Label erstellen mit festem Platz als xy-Koordinate und fester Höhe und Breite
        Bild = tkinter.PhotoImage(file = "w1.gif")
        self.labelEins = tkinter.Label(self,image = Bild)
        self.labelEins.place(x=85, y=75, width=30, height=30)




# bei Klick auf den Knopf ...
    def OnButtonEinsClick(self):
        global Bild

        Bild = tkinter.PhotoImage(file = "w2.gif")
        self.labelEins.configure(image = Bild)





if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Das Fenster')
    app.mainloop()     
