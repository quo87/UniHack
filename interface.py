import pandas as pd
import tkinter as tk
print("hello world")
GUI = tk.Tk()
GUI.title('Scrap Bot 1.0')
submit_button = tk.Button(GUI, text='Submit Keyword',width=25,command=GUI.destroy)
submit_button.pack()
GUI.mainloop()