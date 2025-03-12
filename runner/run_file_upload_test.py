from src.file_upload_test import test_file_upload
from src.utilities import setup_driver, teardown_driver
from src.locators import FileUploadPageLocators as Loc

def run_file_upload_test():
    """
    Executes the file upload test using the filename defined in FileUploadPageLocators.
    """
    driver = setup_driver()

    try:
        print(f"\n Running File Upload Test for: {Loc.FILE_TO_UPLOAD}")
        result = test_file_upload(driver)

        if result:
            print(f"File Upload Test Passed for {Loc.FILE_TO_UPLOAD}")
        else:
            print(f"File Upload Test Failed for {Loc.FILE_TO_UPLOAD}")

    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    run_file_upload_test()
