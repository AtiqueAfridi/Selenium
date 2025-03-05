from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

service = Service()
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://the-internet.herokuapp.com/context_menu")

    # Locate the hot spot
    hot_spot = driver.find_element(By.ID, "hot-spot")

    # Perform a right-click (context click)
    actions = ActionChains(driver)
    actions.context_click(hot_spot).perform()

    # Switch to the alert dialog
    alert = driver.switch_to.alert

    # Get the alert text and print it
    alert_text = alert.text
    print(f"Alert text: {alert_text}")

    # Accept the alert (click OK)
    alert.accept()

    time.sleep(3)  # Keep the browser open for a moment

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()