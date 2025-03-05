from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

service = Service()
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://the-internet.herokuapp.com/")

    # Find the dropdown link and click it
    dropdown_link = driver.find_element(By.LINK_TEXT, "Dropdown")
    dropdown_link.click()

    # Find the dropdown element
    dropdown = Select(driver.find_element(By.ID, "dropdown"))

    # Test selecting by visible text
    dropdown.select_by_visible_text("Option 1")
    selected_option = dropdown.first_selected_option.text
    print(f"Selected by visible text: {selected_option}")
    assert selected_option == "Option 1"
    time.sleep(2)

    # Test selecting by index
    dropdown.select_by_index(2)  # Option 2 (index 2)
    selected_option = dropdown.first_selected_option.text
    print(f"Selected by index: {selected_option}")
    assert selected_option == "Option 2"
    time.sleep(2)

    # Test selecting by value
    dropdown.select_by_value("1") #Option 1
    selected_option = dropdown.first_selected_option.text
    print(f"Selected by value: {selected_option}")
    assert selected_option == "Option 1"

    print("Dropdown test successful!")
    time.sleep(2)  # Pause to see the result

except Exception as e:
    print(f"Dropdown test failed: {e}")

finally:
    driver.quit()