from selenium import webdriver

#driver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
#driver2.session_id = session_id

driver = webdriver.Remote(command_executor='ec89c5c4-3433-48b4-a605-1b47d8021b2e', desired_capabilities={})
driver.session_id='http://127.0.0.1:59289'

print(driver.current_url)