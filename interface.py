import pandas as pd
import tkinter as ttk
#print("hello world")
def getKeyword():
    global word
    word=keyword.get()
    #print(word)

def startGUI():
    GUI.mainloop()

def output():
    print()

word = ''
GUI = ttk.Tk()
GUI.title('Scrap Bot 1.0')
keyword = ttk.Entry(GUI)
keyword.pack()
submit_button = ttk.Button(GUI, text='Submit Keyword',width=25, command = getKeyword)
submit_button.pack()


#startGUI()

