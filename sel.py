from selenium import webdriver
import tkinter as tk
from selenium.webdriver.common.keys import Keys
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
#setup
driver.get('https://google.com')
serch = driver.find_element_by_name("q")
serch.send_keys("123")
serch.send_keys(Keys.RETURN)
driver.quit()