from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service()
driver = webdriver.Chrome(service=service)


# --- Disappearing Elements Test ---
try:
    print("\n--- Disappearing Elements Test ---")
    driver.get("https://the-internet.herokuapp.com/disappearing_elements")
    initial_elements = driver.find_elements(By.TAG_NAME, "li")
    print("Initial number of elements:", len(initial_elements))
    time.sleep(3)  # Add sleep to see the initial elements
    driver.refresh()
    refreshed_elements = driver.find_elements(By.TAG_NAME, "li")
    print("Number of elements after refresh:", len(refreshed_elements))
    if len(initial_elements) != len(refreshed_elements):
        print("Disappearing Elements Test passed")
    else:
        print("Disappearing Elements Test failed: Elements did not disappear")
    time.sleep(3)  # Add sleep to see the result

except Exception as e:
    print("Disappearing Elements Test failed:", e)


finally:
    driver.quit()