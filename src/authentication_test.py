"""
Notebook for testing Authentication on the-internet.herokuapp.com.
"""

from src.utilities import setup_driver, teardown_driver, pause
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import BasicAuthPageLocators, DigestAuthPageLocators
from src.config import BASIC_AUTH_URL, DIGEST_AUTH_URL

def test_basic_auth(driver: WebDriver) -> str:
    """
    Tests Basic Authentication.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        str: The authentication success message, or None if an error occurs.
    """
    try:
        driver.get(BASIC_AUTH_URL)
        message = driver.find_element(*BasicAuthPageLocators.SUCCESS_MESSAGE).text
        return message

    except Exception as e:
        print(f"An error occurred during Basic Authentication test: {e}")
        return None

def test_digest_authentication(driver: WebDriver) -> bool:
    """
    Tests Digest Authentication.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the test passes, False otherwise.
    """
    try:
        print("--- Digest Authentication Test ---")
        driver.get(DIGEST_AUTH_URL)
        success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "p")))
        print("Authentication successful:", success_message.text)
        pause(3)
        return True

    except Exception as e:
        print("Digest Authentication Test failed:", e)
        return False
