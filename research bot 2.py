import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://web.archive.org/web/*/https://www.cnbc.com/finance/")
time.sleep(2)

for a in driver.find_elements_by_xpath('.//a'):
    print(a.get_attribute('href'))



''''
all_links_maybe = driver.find_elements_by_link_text("2022")
print(all_links_maybe)
'''

'''
print(driver.find_element_by_xpath("/html/body").text)
text = driver.find_element_by_xpath("/html/body").text
print("text count: ", text.count("a"))
'''

time.sleep(200)
driver.close()
