""" This is selenium performing checking the broken images"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/") # get to the specified url
link = driver.find_element(By.LINK_TEXT, 'Broken Images') # finds the specified links whose text is Broken Images

link.click()

time.sleep(5)

# Find all image elements on the page
images = driver.find_elements(By.TAG_NAME, 'img') 

# Loop through each image to check its 'src' attribute
for index, image in enumerate(images):
    img_src = image.get_attribute('src')  # Get the 'src' attribute of the image
    print(f"Image {index+1}: {img_src}")


driver.quit()