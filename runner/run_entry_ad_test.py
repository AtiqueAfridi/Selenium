from src.entry_ad_test import test_entry_ad
from src.utilities import setup_driver, teardown_driver

def run_entry_ad_test():
    """
    Executes the Entry Ad popup test.
    """
    driver = setup_driver()

    try:
        print("\nRunning Entry Ad Test...")
        result = test_entry_ad(driver)

        if result:
            print("Entry Ad Test Passed")
        else:
            print("Entry Ad Test Failed")

    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    run_entry_ad_test()
