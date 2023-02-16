from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World!') #finds the input field and types in 'Hello World!'

lightbox = driver.find_element_by_xpath('//*[@id="at-cv-lightbox-close"]')
lightbox.click() #this finds the close button and presses it to close this annoying asf pop up on the website

showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click() #finds the showmessagebutton and clicks it