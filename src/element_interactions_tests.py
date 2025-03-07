from src.utilities import setup_driver, teardown_driver, pause
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from src.locators import Loc


def test_add_remove_elements(driver: WebDriver) -> bool:
    try:
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

        add_button = driver.find_element(*Loc.ADD_BUTTON)
        add_button.click()
        pause(2)

        delete_button_xpath = driver.find_element(*Loc.DELETE_BUTTON_XPATH)
        delete_button_xpath.click()
        pause(3)

        add_button.click()
        delete_button_class = driver.find_element(*Loc.DELETE_BUTTON_CLASS)
        delete_button_class.click()
        pause(5)

        print("Add/Remove Elements test completed successfully.")
        return True

    except Exception as e:
        print(f"An error occurred during Add/Remove Elements test: {e}")
        return False

    

"""
Notebook for testing checkboxes on the-internet.herokuapp.com.
"""



def test_checkboxes(driver: WebDriver) -> bool:
    """
    Tests the checkboxes functionality on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the test passes, False otherwise.
    """
    try:
        driver.get("https://the-internet.herokuapp.com/checkboxes")

        # Locate the checkboxes
        checkbox1 = driver.find_element(*Loc.CHECKBOX_1)
        checkbox2 = driver.find_element(*Loc.CHECKBOX_2)

        # Check initial states
        print(f"Checkbox 1 is selected: {checkbox1.is_selected()}")
        print(f"Checkbox 2 is selected: {checkbox2.is_selected()}")

        # Toggle Checkbox 1 (if unchecked, check it; if checked, uncheck it)
        if not checkbox1.is_selected():
            checkbox1.click()
            print("Checkbox 1 is now checked.")
        else:
            checkbox1.click()
            print("Checkbox 1 is now unchecked.")

        # Toggle Checkbox 2
        if not checkbox2.is_selected():
            checkbox2.click()
            print("Checkbox 2 is now checked.")
        else:
            checkbox2.click()
            print("Checkbox 2 is now unchecked.")

        # Verify states after toggling
        print(f"Checkbox 1 is selected: {checkbox1.is_selected()}")
        print(f"Checkbox 2 is selected: {checkbox2.is_selected()}")

        pause(3)  # Keep the browser open for a moment

        print("Checkboxes test completed successfully.")
        return True

    except Exception as e:
        print(f"An error occurred during Checkboxes test: {e}")
        return False
    

"""
Notebook for testing the context menu on the-internet.herokuapp.com.
"""



def test_context_menu(driver: WebDriver) -> bool:
    """
    Tests the context menu functionality on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the test passes, False otherwise.
    """
    try:
        driver.get("https://the-internet.herokuapp.com/context_menu")

        # Locate the hot spot
        hot_spot = driver.find_element(*Loc.HOT_SPOT)

        # Perform a right-click (context click)
        actions = ActionChains(driver)
        actions.context_click(hot_spot).perform()

        # Switch to the alert dialog
        alert = driver.switch_to.alert

        # Get the alert text and print it
        alert_text = alert.text
        print(f"Alert text: {alert_text}")

        # Accept the alert (click OK)
        alert.accept()

        pause(3)  # Keep the browser open for a moment

        print("Context menu test completed successfully.")
        return True

    except Exception as e:
        print(f"An error occurred during Context menu test: {e}")
        return False
    
"""
Notebook for testing Drag and Drop on the-internet.herokuapp.com.
"""



def test_drag_and_drop(driver: WebDriver) -> bool:
    """
    Tests Drag and Drop on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the test passes, False otherwise.
    """
    try:
        print("\n--- Drag and Drop Test ---")
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        source = driver.find_element(By.ID, "column-a")
        target = driver.find_element(By.ID, "column-b")
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        print("Drag and Drop Test passed")
        pause(3)  # Add pause to see the result
        return True

    except Exception as e:
        print("Drag and Drop Test failed:", e)
        return False
    
"""
Notebook for testing Dropdown on the-internet.herokuapp.com.
"""


from src.locators import DropdownPageLocators as Loc

def test_dropdown(driver: WebDriver) -> bool:
    """
    Tests the dropdown functionality on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the test passes, False otherwise.
    """
    try:
        driver.get("https://the-internet.herokuapp.com/dropdown")

        # Find the dropdown element using the locator
        dropdown = Select(driver.find_element(*Loc.DROPDOWN))

        # Get all available options dynamically
        all_options = [option.text for option in dropdown.options if option.text.strip()]

        if not all_options:
            print("No options found in the dropdown!")
            return False

        # Select the first option by visible text
        dropdown.select_by_visible_text(all_options[0])
        selected_option = dropdown.first_selected_option.text
        print(f"Selected by visible text: {selected_option}")
        assert selected_option == all_options[0]
        pause(1)

        # Select the second option by index (if available)
        if len(all_options) > 1:
            dropdown.select_by_index(1)
            selected_option = dropdown.first_selected_option.text
            print(f"Selected by index: {selected_option}")
            assert selected_option == all_options[1]
            pause(1)

        print("Dropdown test successful!")
        pause(2)
        return True

    except Exception as e:
        print(f"Dropdown test failed: {e}")
        return False
