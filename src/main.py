import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from src.utilities import setup_driver, teardown_driver
from src.locators import Loc
from src.config import AuthConfig, PAGE_URLS

def authenticate_form(driver):
    """Logs into the form authentication page and returns to the base URL."""
    driver.get(PAGE_URLS["base"])
    time.sleep(2)
    driver.get(PAGE_URLS["login"])
    print("Opened Form Authentication page.")
    time.sleep(2)

    driver.find_element(*Loc.FormAuth.USERNAME_FIELD).send_keys(AuthConfig.FORM_AUTH_USERNAME)
    driver.find_element(*Loc.FormAuth.PASSWORD_FIELD).send_keys(AuthConfig.FORM_AUTH_PASSWORD)
    driver.find_element(*Loc.FormAuth.LOGIN_BUTTON).click()
    print("Logged in successfully.")
    time.sleep(2)

    driver.find_element(*Loc.FormAuth.LOGOUT_BUTTON).click()
    print("Logged out successfully.")
    time.sleep(2)

    driver.get(PAGE_URLS["base"])
    print("Returned to Base URL.")

def select_dropdown_option(driver):
    """Navigates to the dropdown page, selects 'Option 2', and returns to base URL."""
    driver.get(PAGE_URLS["dropdown"])
    print("Opened Dropdown page.")
    time.sleep(2)

    dropdown = Select(driver.find_element(*Loc.Dropdown.DROPDOWN_MENU))
    dropdown.select_by_value("2")
    print("Selected 'Option 2'.")
    time.sleep(2)

    driver.get(PAGE_URLS["base"])
    print("Returned to Base URL.")

def forgot_password_test(driver):
    """Navigates to the forgot password page, enters an email, and returns to base URL."""
    driver.get(PAGE_URLS["forgot_password"])
    print("Opened Forgot Password page.")
    time.sleep(2)

    driver.find_element(*Loc.ForgotPassword.EMAIL_INPUT).send_keys("johndoe@gmail.com")
    driver.find_element(*Loc.ForgotPassword.RETRIEVE_BUTTON).click()
    time.sleep(2)

    error_message = driver.find_element(*Loc.ForgotPassword.ERROR_MESSAGE).text
    print(f"Captured message: {error_message}")
    time.sleep(2)

    driver.get(PAGE_URLS["base"])
    print("Returned to Base URL.")

def open_pages_in_tabs(driver):
    """Opens Form Authentication, Dropdown, and Checkboxes pages in new tabs."""
    print("Opening pages in new tabs...")

    pages = [PAGE_URLS["base"], PAGE_URLS["login"], PAGE_URLS["dropdown"], PAGE_URLS["forgot_password"]]

    for url in pages:
        driver.switch_to.new_window("tab")  # ✅ Open in a new tab
        driver.get(url)
        print(f"Opened {url} in a new tab.")
        time.sleep(2)

def open_pages_in_new_windows(driver):
    """Opens Form Authentication, Dropdown, and Checkboxes pages in new Chrome windows."""
    print("Opening pages in new Chrome windows...")

    pages = [PAGE_URLS["login"], PAGE_URLS["dropdown"], PAGE_URLS["forgot_password"]]

    for url in pages:
        driver.switch_to.new_window("window")  # ✅ Open in a new Chrome window
        driver.get(url)
        print(f"Opened {url} in a new window.")
        time.sleep(2)

def close_all_windows(driver):
    """Closes all opened tabs/windows in last opened first closed order with a delay."""
    print("Closing all windows and tabs...")

    handles = driver.window_handles[::-1]  # Reverse order (last opened → first closed)
    
    for handle in handles:
        driver.switch_to.window(handle)
        time.sleep(3)  # ✅ 3-second delay before closing each window
        driver.close()
        print("Closed a window/tab.")

def main():
    """Executes the full Selenium automation test."""
    driver = setup_driver()

    try:
        # ✅ Step 1: Perform required tests
        # authenticate_form(driver)
        # select_dropdown_option(driver)
        # forgot_password_test(driver)

        # ✅ Step 2: Open same pages in new tabs
        open_pages_in_tabs(driver)  

        # ✅ Step 3: Open same pages in new windows
        open_pages_in_new_windows(driver)

        # ✅ Step 4: Close all tabs/windows in last opened first closed order
        close_all_windows(driver)

        print("✅ Test Scenario Completed Successfully!")

    except Exception as e:
        print(f"❌ Test Execution Failed: {e}")

    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    main()
