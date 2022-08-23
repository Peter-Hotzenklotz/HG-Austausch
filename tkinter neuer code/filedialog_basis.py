#!/usr/bin/env python
import tkinter as tk
from tkinter import filedialog

__all__ = ['basis tkMaske.py']



def ask_filename():
    dat=filedialog.askopenfile(
    initialdir = "/",title="zu durchsuchende dateien auswählen",
    filetypes=(("Textdateien","*.txt"),("Ordner(noch nicht implementiert)","*.*"))
    )

class Application(tk.Frame):
    def __init__(self, master=None):
        
        tk.Frame.__init__(self, master)
        self.grid()
        self.__createWidgets()


    def __createWidgets(self):
        
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        
        self.filedialogButton = tk.Button(self, text='Suchmaske erstellen',command=ask_filename)
        self.filedialogButton.bind
        
        self.quitButton.grid()
        self.filedialogButton.grid()




def example():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    example()

"""Ich muss nochmal herausfinden warum in diesem Fall die Datei example
ausgeführt wird auch wenn der Dateiname nicht derselbe ist. Dafür schau ich
nochmal ins Python Handbuch, da sollte ich mir mal ein neueres suchen
auch wenn die unterschiede geringfügig sind.
"""
