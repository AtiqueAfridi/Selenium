"""
Notebook for testing the Challenging DOM on the-internet.herokuapp.com.
"""

from src.utilities import setup_driver, teardown_driver, pause
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

def test_challenging_dom(driver: WebDriver) -> bool:
    """
    Tests the Challenging DOM functionality on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the test passes, False otherwise.
    """
    try:
        driver.get("https://the-internet.herokuapp.com/challenging_dom")

        # Example 1: Locate and print a cell value (dynamic)
        cell_value = driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[3]").text
        print(f"Cell value: {cell_value}")

        # Example 2: Locate and click a button (dynamic ID)
        edit_button = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[7]/a[1]")
        edit_button.click()

        # Example 3: Locate and click the blue button
        blue_button = driver.find_element(By.CSS_SELECTOR, ".button")
        blue_button.click()

        # Example 4: Locate and click the green button
        green_button = driver.find_element(By.CSS_SELECTOR, ".button.success")
        green_button.click()

        # Example 5: Locate and click the red button
        red_button = driver.find_element(By.CSS_SELECTOR, ".button.alert")
        red_button.click()

        pause(3)  # Keep the browser open for a moment

        print("Challenging DOM test completed successfully.")
        return True

    except Exception as e:
        print(f"An error occurred during Challenging DOM test: {e}")
        return False

def main():
    """
    Main function to run the Challenging DOM test.
    """
    driver = setup_driver()
    try:
        if test_challenging_dom(driver):
            print("Challenging DOM test passed.")
        else:
            print("Challenging DOM test failed.")

    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    main()