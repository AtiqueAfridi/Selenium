"""This is selenium performing the A/B testing on the url https://the-internet.herokuapp.com/"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time 

service = Service()
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/")
link  = driver.find_element(By.LINK_TEXT, 'A/B Testing') #Finds the hyper link using its text

# Actionchain are a way to automate the low level interactions
action = ActionChains(driver) #creates an action chain object 


action.move_to_element(link).perform()  # Moves the cursor to the desired link


time.sleep(5)
link.click() #Clicks the link with the "A/B Testing" text

time.sleep(5)

driver.quit() # quits the driver and its functionality