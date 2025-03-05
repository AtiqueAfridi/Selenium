from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service()
driver = webdriver.Chrome(service=service)

# --- Digest Authentication Test ---
try:
    print("--- Digest Authentication Test ---")
    url = "https://admin:admin@the-internet.herokuapp.com/digest_auth"
    driver.get(url)
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "p"))
    )
    print("Authentication successful:", success_message.text)
    time.sleep(3)  # Add sleep to see the result

except Exception as e:
    print("Digest Authentication Test failed:", e)

finally:
    driver.quit()