from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from src.utilities import setup_driver, teardown_driver, pause
from src.locators import Loc
from src.config import AuthConfig, PAGE_URLS

def test_form_authentication(driver: WebDriver) -> bool:
    """
    Tests form authentication on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    try:
        # Use `PAGE_URLS` for dynamic URL handling
        login_url = PAGE_URLS["login"]
        driver.get(login_url)
        print(f"Opened URL: {login_url}")

        wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

        # Wait for Username Field
        username_field = wait.until(EC.visibility_of_element_located(Loc.FormAuth.USERNAME_FIELD))
        username_field.send_keys(AuthConfig.FORM_AUTH_USERNAME)

        # Wait for Password Field
        password_field = wait.until(EC.visibility_of_element_located(Loc.FormAuth.PASSWORD_FIELD))
        password_field.send_keys(AuthConfig.FORM_AUTH_PASSWORD)

        # Wait for Login Button
        login_button = wait.until(EC.element_to_be_clickable(Loc.FormAuth.LOGIN_BUTTON))
        login_button.click()

        # Wait for Success Message
        success_message = wait.until(EC.presence_of_element_located(Loc.FormAuth.SUCCESS_MESSAGE)).text
        print(f"Login Successful: {success_message}")
        return True

    except Exception as e:
        print(f"Login Failed: {e}")
        print(f"Page Source:\n{driver.page_source}")  # Debugging step
        return False
