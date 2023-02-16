from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox() #using firefox

url = 'https://www.bestbuy.com/site/playstation-5/ps5-consoles/pcmcat1587395025973.c?id=pcmcat1587395025973'
driver.remote()

buttons = driver.find_elements_by_class_name('btn')

def addCart():
    id= 1
    if (buttons):
        for i in range(0, len(buttons)):
            print("id=" + str(id) + " " + str(buttons[i]))
            id = id+1
#driver.refresh()

addCart()

driver.close()