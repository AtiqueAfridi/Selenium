from src.file_upload_test import test_file_upload
from src.utilities import setup_driver, teardown_driver

def run_file_upload_test():
    driver = setup_driver()
    try:
        print("\nRunning File Upload Test...")
        result = test_file_upload(driver)

        if result:
            print("File Upload Test Passed")
        else:
            print("File Upload Test Failed")

    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    run_file_upload_test()
