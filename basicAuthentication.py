""" This is selenium performing the Basic Authentication"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
driver = webdriver.Chrome(service=service)

try:
    # Embed credentials in the URL
    url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
    driver.get(url)

    # Verify that you've successfully authenticated
    message = driver.find_element(By.XPATH, "//div[@class='example']/p").text
    print(message)

    time.sleep(3)  # Optional delay

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()