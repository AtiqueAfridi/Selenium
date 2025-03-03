from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# Set up ChromeDriver service
service = Service()

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service)

try:
    # Open the URL
    driver.get("https://sites.google.com/view/atiqueabdullah/")

    time.sleep(5) #Sleep for 5 seconds.

    #Optional: Get the title of the webpage and print it.
    title = driver.title
    print(f"Page title: {title}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()