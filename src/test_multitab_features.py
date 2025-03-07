from src.utilities import setup_driver, teardown_driver, pause
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

def test_checkboxes(driver: WebDriver):
    """
    Opens the checkboxes page in a new tab and tests checkbox interactions.
    """
    try:
        driver.execute_script("window.open('https://the-internet.herokuapp.com/checkboxes', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])  # Switch to the last opened tab

        checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
        checkbox2 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")

        if not checkbox1.is_selected():
            checkbox1.click()
        if not checkbox2.is_selected():
            checkbox2.click()

        print("Checkboxes test completed.")
        pause(2)

    except Exception as e:
        print(f"Error in checkboxes test: {e}")

def test_dropdown(driver: WebDriver):
    """
    Opens the dropdown page in another new tab and tests dropdown selections.
    """
    try:
        driver.execute_script("window.open('https://the-internet.herokuapp.com/dropdown', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])  # Switch to the last opened tab

        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_index(1)
        print(f"Dropdown selected: {dropdown.first_selected_option.text}")

        pause(2)

    except Exception as e:
        print(f"Error in dropdown test: {e}")

def test_drag_and_drop(driver: WebDriver):
    """
    Opens the drag-and-drop page in a new tab and tests drag-and-drop interactions.
    """
    try:
        driver.execute_script("window.open('https://the-internet.herokuapp.com/drag_and_drop', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])  # Switch to the last opened tab

        source = driver.find_element(By.ID, "column-a")
        target = driver.find_element(By.ID, "column-b")

        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()

        print("Drag-and-Drop test completed.")
        pause(2)

    except Exception as e:
        print(f"Error in drag-and-drop test: {e}")

def run_multitab_tests():
    driver = setup_driver()
    try:
        print("\nRunning Checkboxes Test in New Tab...")
        test_checkboxes(driver)

        print("\nRunning Dropdown Test in Another New Tab...")
        test_dropdown(driver)

        print("\nRunning Drag-and-Drop Test in Another New Tab...")
        test_drag_and_drop(driver)

        print("\nAll multi-tab tests completed successfully.")

    # Prevent script from exiting & closing the browser
        input("Press Enter to close the browser and end the session...")

    except Exception as e:
        print(f"Error during multi-tab test execution: {e}")

    finally:
        teardown_driver(driver)  # This will only execute after you press Enter