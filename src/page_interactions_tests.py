"""
Notebook for testing broken images on the-internet.herokuapp.com.
"""

from src.utilities import setup_driver, teardown_driver, pause
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import requests


def test_a_b_testing(driver: WebDriver) -> str:
    """
    Tests the A/B Testing page on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        str: The heading text of the A/B Testing page.
    """
    try:
        driver.get("https://the-internet.herokuapp.com/abtest")

        # Locate the heading element and extract text
        heading_text = driver.find_element(By.TAG_NAME, "h3").text
        print(f"A/B Test Page Heading: {heading_text}")

        pause(2)  # Short pause to observe result
        return heading_text

    except Exception as e:
        print(f"An error occurred in A/B Testing: {e}")
        return None


def test_broken_images(driver: WebDriver) -> bool:
    """
    Tests for broken images on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the test passes (no broken images), False otherwise.
    """
    try:
        driver.get("https://the-internet.herokuapp.com/broken_images")

        images = driver.find_elements(By.TAG_NAME, 'img')
        broken_images_found = False

        for index, image in enumerate(images):
            img_src = image.get_attribute('src')
            print(f"Checking Image {index + 1}: {img_src}")

            try:
                response = requests.head(img_src, allow_redirects=True)
                if response.status_code >= 400:
                    print(f"  Image {index + 1} is broken (status code: {response.status_code})")
                    broken_images_found = True
            except requests.exceptions.RequestException as e:
                print(f"  Error checking image {index + 1}: {e}")
                broken_images_found = True

        if not broken_images_found:
            print("No broken images found.")
            return True
        else:
            return False

    except Exception as e:
        print(f"An error occurred during Broken Images test: {e}")
        return False
    


"""
Notebook for testing Disappearing Elements on the-internet.herokuapp.com.
"""


from selenium.webdriver.remote.webdriver import WebDriver

def test_disappearing_elements(driver: WebDriver) -> bool:
    """
    Tests Disappearing Elements on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the test passes, False otherwise.
    """
    try:
        print("\n--- Disappearing Elements Test ---")
        driver.get("https://the-internet.herokuapp.com/disappearing_elements")
        initial_elements = driver.find_elements(By.TAG_NAME, "li")
        print("Initial number of elements:", len(initial_elements))
        pause(3)  # Add pause to see the initial elements
        driver.refresh()
        refreshed_elements = driver.find_elements(By.TAG_NAME, "li")
        print("Number of elements after refresh:", len(refreshed_elements))
        if len(initial_elements) != len(refreshed_elements):
            print("Disappearing Elements Test passed")
            return True
        else:
            print("Disappearing Elements Test failed: Elements did not disappear")
            return False

    except Exception as e:
        print("Disappearing Elements Test failed:", e)
        return False
    
"""
Notebook for testing the Challenging DOM on the-internet.herokuapp.com.
"""


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