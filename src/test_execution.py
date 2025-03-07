from src.authentication_test import test_basic_auth
from src.element_interactions_tests import test_add_remove_elements
from src.element_interactions_tests import test_checkboxes, test_dropdown
from src.page_interactions_tests import test_a_b_testing

from src.utilities import setup_driver, teardown_driver, pause

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


def run_tests():
    driver = setup_driver()
    try:
        print("\nRunning Checkboxes Test in New Tab...")
        test_checkboxes(driver)

        print("\nRunning Dropdown Test in Another New Tab...")
        test_dropdown(driver)

        # Switch back to the first tab before quitting
        driver.switch_to.window(driver.window_handles[0])
        print("\n Multi-tab tests completed successfully.")

    finally:
        teardown_driver(driver)


# def run_tests():
#     driver = setup_driver()
#     try:
#         print("\nRunning A/B Testing...")
#         ab_test_result = test_a_b_testing(driver)
#         print(f"A/B Testing Result: {ab_test_result}")
#         pause(2)
#         driver.back()

#         print("\nRunning Add/Remove Elements Test...")
#         if test_add_remove_elements(driver):
#             print("Add/Remove Elements Test Passed")
#         else:
#             print("Add/Remove Elements Test Failed")
#         pause(2)
#         driver.back()

#         print("\nRunning Basic Authentication Test...")
#         auth_result = test_basic_auth(driver)
#         if auth_result:
#             print(f"Basic Authentication Successful: {auth_result}")
#         else:
#             print("Basic Authentication Test Failed")
#         pause(2)

#     finally:
#         teardown_driver(driver)
