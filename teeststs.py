from selenium import webdriver
from time import sleep
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.archive.org/web/*/https://www.cnbc.com/finance/")
sleep(5)
list_links = driver.find_elements_by_tag_name('a')

for i in list_links:
        print(i.get_attribute('href'))



sleep(3000)
driver.quit()