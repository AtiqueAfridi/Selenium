import os
import time
from src.utilities import setup_driver, teardown_driver, DOWNLOADS_DIR
from src.locators import FileDownloadPageLocators as Loc
from selenium.webdriver.remote.webdriver import WebDriver

def test_file_download(driver: WebDriver) -> bool:
    """
    Tests file download functionality on the-internet.herokuapp.com.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        bool: True if the file is downloaded successfully, False otherwise.
    """
    try:
        driver.get("https://the-internet.herokuapp.com/download")

        # Click the "billie.jpg" link to download the file
        driver.find_element(*Loc.BILLIE_JPG_LINK).click()
        print("Download initiated for billie.jpg")

        # Wait for the file to appear in the downloads directory
        downloaded_file_path = os.path.join(DOWNLOADS_DIR, "billie.jpg")
        timeout = 15  # Max wait time in seconds

        for _ in range(timeout):
            if os.path.exists(downloaded_file_path):
                print("File downloaded successfully: billie.jpg")
                return True
            time.sleep(1)  # Wait a second before checking again

        print("Download failed: File not found after timeout")
        return False

    except Exception as e:
        print(f"Error during file download test: {e}")
        return False
