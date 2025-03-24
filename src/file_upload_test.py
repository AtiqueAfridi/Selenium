import os
from selenium.webdriver.remote.webdriver import WebDriver
from src.utilities import DOWNLOADS_DIR
from src.locators import FileUploadPageLocators as Loc
from src.config import PAGE_URLS  # Importing URLs from config

def test_file_upload(driver: WebDriver) -> bool:
    """
    Tests file upload functionality on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the file is uploaded successfully, False otherwise.
    """
    try:
        driver.get(PAGE_URLS["file_upload"])  # Load file upload page

        # Get the file name dynamically from locators
        filename = Loc.FILE_TO_UPLOAD  
        file_path = os.path.join(DOWNLOADS_DIR, filename)

        # Ensure the file exists before uploading
        if not os.path.exists(file_path):
            print(f"Error: File not found - {file_path}")
            return False

        # Locate the file input field and upload the selected file
        driver.find_element(*Loc.FILE_INPUT).send_keys(file_path)
        print(f"File selected for upload: {file_path}")

        # Click the upload button
        driver.find_element(*Loc.UPLOAD_BUTTON).click()

        # Verify successful upload
        upload_text = driver.find_element(*Loc.UPLOAD_SUCCESS_TEXT).text
        if "File Uploaded!" in upload_text:
            print(f"Success: {filename} uploaded successfully!")
            return True
        else:
            print(f"Error: Upload failed for {filename}.")
            return False

    except Exception as e:
        print(f"Exception in file upload test: {e}")
        return False
