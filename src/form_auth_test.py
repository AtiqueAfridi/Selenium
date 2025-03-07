from src.utilities import setup_driver, teardown_driver, pause
from src.locators import FormAuthPageLocators as Loc
from src.config import AuthConfig
from selenium.webdriver.remote.webdriver import WebDriver

def test_form_authentication(driver: WebDriver) -> bool:
    """
    Tests form authentication on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    try:
        driver.get("https://the-internet.herokuapp.com/login")

        # Locate username and password fields & login button
        driver.find_element(*Loc.USERNAME_FIELD).send_keys(AuthConfig.FORM_AUTH_USERNAME)
        driver.find_element(*Loc.PASSWORD_FIELD).send_keys(AuthConfig.FORM_AUTH_PASSWORD)
        driver.find_element(*Loc.LOGIN_BUTTON).click()

        # Check if login was successful
        success_message = driver.find_element(*Loc.SUCCESS_MESSAGE).text
        print(f"Login Successful: {success_message}")
        return True

    except Exception as e:
        print(f"Login Failed: {e}")
        return False
