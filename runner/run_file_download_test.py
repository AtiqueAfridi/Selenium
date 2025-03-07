from src.file_download_test import test_file_download
from src.utilities import setup_driver, teardown_driver

def run_file_download_test():
    driver = setup_driver()
    try:
        print("\n Running File Download Test...")
        result = test_file_download(driver)
        
        if result:
            print("File Download Test Passed")
        else:
            print("File Download Test Failed")

    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    run_file_download_test()
