#!/usr/bin/env python 1
import tkinter as tk
from tkinter import filedialog

# @ HG: Ich habe die Aufaben jeweils in funktionen gepackt am codeende sind die Funktionsaufrufe kupiert und
# Auskommentiert. JHmainwindow bzw. Aufabe 3 habe ich bereits etwas erweitert und ist nicht Auskommentiert.

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        winapp = self
        # startWindow(winapp)

# def startWindow(winapp):
#     winapp.grid()
#
#     winapp.master.title('Sample application')
#     winapp.quitButton = tk.Button(winapp, text='Quit', command=winapp.quit)
#     winapp.quitButton.grid()

def Aufabe1():
    app = Application()
    app.mainloop()

class JHWindow(Application):
    def __init__(self):
        Application.__init__(self)

    # hier wird eine methode definiert
    def startWindow(self):
        self.grid()
        # self.master.title('Titel von JHWindow')
        # self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        # self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        # self.quitButton.grid()

def aufabe2():
    jhWin = JHWindow()
    jhWin.startWindow()
    jhWin.mainloop()

# aufabe2()

class JHMainWindow(JHWindow):
    def __init__(self):
        JHWindow.__init__(self)


    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()
        self.filedialogButton = tk.Button(self, text='filedialogButton', command=self.ask_filename)
        self.filedialogButton.grid()

    def ask_filename(self):
        ZielListe = []
        print("inside Askfilename")
        dat = filedialog.askopenfile(
            initialdir="/", title="Ausgangsbuch wählen (wählen sie ihr Lieblingsbuch).",
            filetypes=(("Romane im Format", "*.pdf"), ("Ordner(noch nicht implementiert)", "*.*"))
        )
        # print(dat)
        ZielListe.append(dat)
        print("ZielListe=", str(ZielListe))

        # @HG Hier könnte ich eher versuchen mit "get" Methoden die einzelnen Daten herauszulesen,
        # vor allem interessiert mich der Pfad und der Name des PDF-Dokuments/Buches.
        # Schließlich ist das der Ort und das Buch welches später im Proramm durchsucht wird.
        # Vielleicht ist es hier schon sinnvoll die Daten in eine Datenbank zu übertragen.
        # Vorher habe ich daten stumpf in .txt dateien geschrieben und wieder ausgelesen.




    def setTitel(self,Überschrift):
        self.master.title(Überschrift)






def aufgabe3():
    jhMainWin = JHMainWindow()
    jhMainWin.startWindow()
    jhMainWin.createWidgets()
    jhMainWin.mainloop()

# aufgabe3()


def nametest1():
    nametestWin = JHMainWindow()
    nametestWin.setTitel("Nametest1")
    nametestWin.startWindow()
    nametestWin.createWidgets()
    nametestWin.mainloop()

# nametest1()

def nametest2():
    nametest2Win = JHMainWindow()
    nametest2Win.master.title("Nametest2")
    nametest2Win.startWindow()
    nametest2Win.createWidgets()
    nametest2Win.mainloop()

# nametest2()


# def ask_filename():
#     print("askfilename")

# aufabe1()
# aufabe2()
aufgabe3()
# nametest1()
# nametest2()
