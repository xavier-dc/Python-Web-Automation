#chrome.exe -remote-debugging-port=1234 --user-data-dir="C:\Users\Hiten\OneDrive\Desktop\GoogleProfile"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)/Google/Chrome/Application/chromedriver_win32/chromedriver.exe')

driverOptions = Options()
driverOptions.add_experimental_option("debuggerAddress", "localhost:1234")

driver2 = webdriver.Chrome(options=driverOptions)

driver2.get("https://www.facebook.com")