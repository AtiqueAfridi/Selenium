from src.authentication_test import test_basic_auth, test_digest_authentication
from src.utilities import setup_driver, teardown_driver, pause

def run_auth_tests():
    driver = setup_driver()
    try:
        print("\nRunning Basic Authentication Test...")
        basic_auth_result = test_basic_auth(driver)
        if basic_auth_result:
            print(f"Basic Authentication Successful: {basic_auth_result}")
        else:
            print("Basic Authentication Test Failed")

        pause(2)

        print("\nRunning Digest Authentication Test...")
        digest_auth_result = test_digest_authentication(driver)
        if digest_auth_result:
            print("Digest Authentication Test Passed")
        else:
            print("Digest Authentication Test Failed")

    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    run_auth_tests()
