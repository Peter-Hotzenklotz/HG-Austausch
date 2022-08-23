#!/usr/bin/env python
import tkinter as tk

__all__ = ['basis tkMaske.py']

class Application(tk.Frame):
    def __init__(self, master=None):
        
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()

def example():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    example()
