"""This is selenium performg the Checkboxes test"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/webdriver/chromedriver.exe"  #Path to driver exe

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)


try:
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # Locate the checkboxes
    checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
    checkbox2 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")

    # Check initial states
    print(f"Checkbox 1 is selected: {checkbox1.is_selected()}")
    print(f"Checkbox 2 is selected: {checkbox2.is_selected()}")

    # Toggle Checkbox 1 (if unchecked, check it; if checked, uncheck it)
    if not checkbox1.is_selected():
        checkbox1.click()
        print("Checkbox 1 is now checked.")
    else:
        checkbox1.click()
        print("Checkbox 1 is now unchecked.")

    # Toggle Checkbox 2
    if not checkbox2.is_selected():
        checkbox2.click()
        print("Checkbox 2 is now checked.")
    else:
        checkbox2.click()
        print("Checkbox 2 is now unchecked.")

    # Verify states after toggling
    print(f"Checkbox 1 is selected: {checkbox1.is_selected()}")
    print(f"Checkbox 2 is selected: {checkbox2.is_selected()}")

    time.sleep(3)  # Keep the browser open for a moment

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
