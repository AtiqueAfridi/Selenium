import os
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utilities import DOWNLOADS_DIR
from src.locators import FileDownloadPageLocators as Loc
from src.config import PAGE_URLS  

def test_file_download(driver: WebDriver, target_filename: str, timeout: int = 15) -> bool:
    """
    Downloads a specific file from the download page and verifies the download.

    Args:
        driver (WebDriver): The WebDriver instance.
        target_filename (str): The name of the file to download.
        timeout (int, optional): Maximum wait time (in seconds) for the file to appear. Defaults to 15.

    Returns:
        bool: True if the file is downloaded successfully, False otherwise.
    """
    try:
        driver.get(PAGE_URLS["file_download"])  # Ensure the URL is correct

        # Wait for all file links to load
        wait = WebDriverWait(driver, timeout)
        file_links = wait.until(EC.presence_of_all_elements_located(Loc.FILE_LINKS))

        # Search for the specific file
        target_file = None
        for file_link in file_links:
            if file_link.text.strip() == target_filename:
                target_file = file_link
                break

        if not target_file:
            print(f"File '{target_filename}' not found on the page.")
            return False

        # Click to download
        target_file.click()
        print(f"Download initiated for: {target_filename}")

        # Construct the expected file path
        downloaded_file_path = os.path.join(DOWNLOADS_DIR, target_filename)

        # Wait for the file to appear in the downloads directory
        for _ in range(timeout):
            if os.path.exists(downloaded_file_path):
                print(f"File downloaded successfully: {target_filename}")
                return True
            time.sleep(1)

        print(f"Download failed: {target_filename} not found after {timeout} seconds.")
        return False

    except Exception as e:
        print(f"Error during file download test: {e}")
        return False
