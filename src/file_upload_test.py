import os
from src.utilities import setup_driver, teardown_driver, DOWNLOADS_DIR
from src.locators import FileUploadPageLocators as Loc
from selenium.webdriver.remote.webdriver import WebDriver

def test_file_upload(driver: WebDriver) -> bool:
    """
    Tests file upload functionality on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the file is uploaded successfully, False otherwise.
    """
    try:
        driver.get("https://the-internet.herokuapp.com/upload")

        # Path to the file we downloaded earlier
        file_path = os.path.join(DOWNLOADS_DIR, "billie.jpg")

        # Ensure the file exists before trying to upload
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return False

        # Locate the file input field and upload the image
        driver.find_element(*Loc.FILE_INPUT).send_keys(file_path)
        print(f"File selected for upload: {file_path}")

        # Click the upload button
        driver.find_element(*Loc.UPLOAD_BUTTON).click()

        # Verify successful upload
        upload_text = driver.find_element(*Loc.UPLOAD_SUCCESS_TEXT).text
        if "File Uploaded!" in upload_text:
            print("File upload successful!")
            return True
        else:
            print("File upload failed!")
            return False

    except Exception as e:
        print(f"Error during file upload test: {e}")
        return False
