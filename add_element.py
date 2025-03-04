"""This is selenium performing the add and remove functionality on the url https://the-internet.herokuapp.com/"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/") # get to the specified url
link = driver.find_element(By.LINK_TEXT, 'Add/Remove Elements') # finds the specified links

link.click() # clicks the link

addElement = driver.find_element(By.XPATH, "//button[text()= 'Add Element']") #Find the add button using XPATH
addElement.click() # click the button


time.sleep(2)

deleteElement = driver.find_element(By.XPATH, "//button [text() = 'Delete']") 
deleteElement.click()

time.sleep(3)

addElement.click()
deleteElement = driver.find_element(By.CLASS_NAME, "added-manually") #Finds the  delete button by class name

deleteElement.click()

time.sleep(5)

driver.quit()
