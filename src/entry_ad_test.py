import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utilities import setup_driver, teardown_driver
from src.locators import Loc
from src.config import PAGE_URLS

def test_entry_ad(driver: WebDriver) -> bool:
    """
    Tests the Entry Ad popup on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the modal is detected and successfully closed, False otherwise.
    """
    try:
        driver.get(PAGE_URLS["entry_ad"])  # Using dynamic URL from config
        print("Opened Entry Ad page.")

        wait = WebDriverWait(driver, 10)

        # Wait for the modal to be visible
        modal = wait.until(EC.visibility_of_element_located(Loc.EntryAd.MODAL))
        print("Entry Ad modal appeared.")

        # Close the modal if present
        close_button = wait.until(EC.element_to_be_clickable(Loc.EntryAd.MODAL_CLOSE_BUTTON))
        close_button.click()
        print("Closed Entry Ad modal.")

        # Ensure modal is no longer visible
        try:
            wait.until(EC.invisibility_of_element_located(Loc.EntryAd.MODAL))
            print("Entry Ad modal successfully closed.")
            
            # Keep the browser open for 5 seconds after closing the modal
            time.sleep(5)
            return True
        except:
            print("Error: Modal did not close properly.")
            return False

    except Exception as e:
        print(f"Entry Ad test failed: {e}")
        return False
