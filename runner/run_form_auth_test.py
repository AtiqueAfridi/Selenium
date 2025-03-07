from src.form_auth_test import test_form_authentication
from src.utilities import setup_driver, teardown_driver

def run_form_auth_test():
    driver = setup_driver()
    try:
        print("\n🔹 Running Form Authentication Test...")
        result = test_form_authentication(driver)
        
        if result:
            print("Form Authentication Test Passed")
        else:
            print("Form Authentication Test Failed")

    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    run_form_auth_test()
