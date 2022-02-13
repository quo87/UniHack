from selenium import webdriver
from time import sleep
import pandas as pd
import tkinter as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



    #print(word)
GUI = ttk.Tk()
def startGUI():
    GUI.mainloop()


word = ''

GUI.title('Scrap Bot 1.0')





keyword = input("enter ur keyword: ")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.archive.org/web/*/https://www.cnbc.com/finance/")
sleep(5)
list_links = driver.find_elements_by_tag_name('a')
repeats = []
data = []
loopy = []
for i in list_links:
        loopy.append(i.get_attribute('href'))


for i in loopy:
        link = str(i)
        print(i)
        if link in repeats:
                print("goober dectected, skip engaged")
                continue
        elif link.count("2022") >= 1:
                repeats.append(link)
                driver.get(i)
                sleep(5)
                text = driver.find_element_by_xpath("/html/body").text
                data.append(text.count(keyword))
                driver.back()
                sleep(2)
                print(data)


figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, GUI)
chart_type.get_tk_widget().pack()
df = pd.DataFrame(data,range(0,len(data)))
df.plot(kind='line', legend=True, ax=ax)
ax.set_title('Word Count')

GUI.mainloop()

sleep(3000)
driver.quit()
