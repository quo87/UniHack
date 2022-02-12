print("hello world")
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://google.com") #go to google
search = driver.find_element_by_name("q")
search.send_keys("the ocean currents")
search.send_keys(Keys.RETURN)

search_results = driver.find_element_by_id("rso")
print(search_results.text)
#with this, now I'm able to get the search results on a page, now I'll try to get the individually


time.sleep(15)
driver.quit()