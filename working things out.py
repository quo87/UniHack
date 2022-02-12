print("hello world")
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://google.com") #go to google
search = driver.find_element_by_name("q")
search.send_keys("beeeeeeeans")
search.send_keys(Keys.RETURN)
time.sleep(10)
'''
#bring in search results
print(driver.page_source) #prints out the page source, allows us to scrape and access the entire website
'''

driver.quit()

