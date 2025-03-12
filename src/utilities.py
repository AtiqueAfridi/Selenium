"""
Utility functions and common setup for Selenium notebooks.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Add this import to fix the error
import time
import os

# Set up the download directory
DOWNLOADS_DIR = os.path.join(os.getcwd(), "downloads")  # Saves to "downloads/" in project root
os.makedirs(DOWNLOADS_DIR, exist_ok=True)  # Ensure directory exists


def setup_driver():
    """Sets up and returns a Chrome WebDriver instance with download preferences."""
    chrome_options = Options()
    
    # Configure Chrome to automatically download files
    prefs = {
        "download.default_directory": DOWNLOADS_DIR,  # Set default download folder
        "download.prompt_for_download": False,  # Disable download pop-ups
        "download.directory_upgrade": True,  # Auto-upgrade downloads
        "safebrowsing.enabled": True  # Avoid security prompts
    }
    chrome_options.add_experimental_option("prefs", prefs)

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def teardown_driver(driver):
    """Quits the WebDriver instance."""
    if driver:
        driver.quit()

def pause(seconds):
    """Pauses execution for the specified number of seconds."""
    time.sleep(seconds)