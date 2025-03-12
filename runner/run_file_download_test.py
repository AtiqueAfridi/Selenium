from src.file_download_test import test_file_download
from src.utilities import setup_driver, teardown_driver

def run_file_download_test():
    driver = setup_driver()
    target_filename = "hello.rtf"  # Change this to the file you want to download

    try:
        print("\n Running File Download Test...")
        result = test_file_download(driver, target_filename)

        if result:
            print(f"File Download Test Passed for {target_filename}")
        else:
            print(f"File Download Test Failed for {target_filename}")

    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    run_file_download_test()
