"""This is selenium performing the Challenging DOM Test"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://the-internet.herokuapp.com/challenging_dom")

    # Example 1: Locate and print a cell value (dynamic)
    # Using XPath to locate the 2nd row, 3rd cell
    cell_value = driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[3]").text
    print(f"Cell value: {cell_value}")

    # Example 2: Locate and click a button (dynamic ID)
    # Using XPath to locate the "edit" button in the first row
    edit_button = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[7]/a[1]")
    edit_button.click()

    #Example 3: Locate and click the blue button
    blue_button = driver.find_element(By.CSS_SELECTOR, ".button")
    blue_button.click()

    #Example 4: Locate and click the green button
    green_button = driver.find_element(By.CSS_SELECTOR, ".button.success")
    green_button.click()

    #Example 5: Locate and click the red button
    red_button = driver.find_element(By.CSS_SELECTOR, ".button.alert")
    red_button.click()

    time.sleep(5)  # Keep the browser open for a moment

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    #driver.quit() #remove quit if you want to keep the browser open.
    pass