import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pyautogui
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.archive.org/web/*/https://www.cnbc.com/finance/")
time.sleep(3)





print(search)
'''
pyautogui.hotkey('ctrl', 'f')
a = ActionChains(driver)
time.sleep(2)
pyautogui.typewrite('Feb')

'''
time.sleep(200)
driver.close()
