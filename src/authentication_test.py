"""
Notebook for testing Basic Authentication on the-internet.herokuapp.com (with functions).
"""

from src.utilities import setup_driver, teardown_driver, pause
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver #Explicit type hinting.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import BasicAuthPageLocators, DigestAuthPageLocators

def test_basic_auth(driver: WebDriver) -> str:
    """
    Tests Basic Authentication on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        str: The authentication success message, or None if an error occurs.
    """
    try:
        url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
        driver.get(url)

        message = driver.find_element(*BasicAuthPageLocators.SUCCESS_MESSAGE).text
        return message

    except Exception as e:
        print(f"An error occurred during Basic Authentication test: {e}")
        return None
    

"""
Notebook for testing Digest Authentication on the-internet.herokuapp.com.
"""



def test_digest_authentication(driver: WebDriver) -> bool:
    """
    Tests Digest Authentication on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the test passes, False otherwise.
    """
    try:
        print("--- Digest Authentication Test ---")
        url = "https://admin:admin@the-internet.herokuapp.com/digest_auth"
        driver.get(url)
        success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "p")))
        print("Authentication successful:", success_message.text)
        pause(3)  # Add pause to see the result
        return True

    except Exception as e:
        print("Digest Authentication Test failed:", e)
        return False
