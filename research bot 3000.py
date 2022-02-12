from selenium import webdriver
from time import sleep
keyword = input("enter ur keyword: ")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.archive.org/web/*/https://www.cnbc.com/finance/")
sleep(5)
list_links = driver.find_elements_by_tag_name('a')
repeats = []
data = []
for i in list_links:
        link = str(i.get_attribute('href'))
        print(i.get_attribute('href'))
        if link in repeats:
                print("goober dectected, skip engaged")
                continue
        elif link.count("2022") >= 1:
                repeats.append(link)
                i.click()
                sleep(5)
                text = driver.find_element_by_xpath("/html/body").text
                data.append(text.count(keyword))


sleep(3000)
driver.quit()