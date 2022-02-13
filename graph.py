import matplotlib.pyplot as plt
import tkinter as tk
import test
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = tk.Tk()
data = test.generate_data(0,30)
print(data)
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, root)
chart_type.get_tk_widget().pack()
df = pd.DataFrame(data,range(0,len(data)))
#print(df)
df.plot(kind='line', legend=True, ax=ax)
ax.set_title('Word Count')

root.mainloop()




