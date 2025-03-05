from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service()
driver = webdriver.Chrome(service=service)


# --- Drag and Drop Test ---
try:
    print("\n--- Drag and Drop Test ---")
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    source = driver.find_element(By.ID, "column-a")
    target = driver.find_element(By.ID, "column-b")
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    print("Drag and Drop Test passed")
    time.sleep(3)  # Add sleep to see the result

except Exception as e:
    print("Drag and Drop Test failed:", e)

finally:
    driver.quit()
