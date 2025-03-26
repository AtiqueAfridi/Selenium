import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.utilities import setup_driver, teardown_driver, DOWNLOADS_DIR
from src.locators import Loc
from src.config import AuthConfig, PAGE_URLS


def open_pages(driver):
    """Opens pages in new tabs or new windows, storing handles in a dictionary."""
    print("Opening pages...")

    tab_pages = {
        "Form Authentication": PAGE_URLS["login"],
        "Entry Ad": PAGE_URLS["entry_ad"],
        "Context Menu": PAGE_URLS["context_menu"]
    }

    window_pages = {
        "Digest Authentication": PAGE_URLS["digest_auth"],
        "File Upload": PAGE_URLS["file_upload"]
    }

    browser_sessions = {}

    # Open pages in new tabs
    for page_name, url in tab_pages.items():
        driver.execute_script("window.open(arguments[0], '_blank');", url)
        handle = driver.window_handles[-1]
        browser_sessions[handle] = page_name
        print(f"✅ Opened {page_name} in a new tab.")
        time.sleep(5)

    # Open pages in new windows
    for page_name, url in window_pages.items():
        driver.execute_script("window.open(arguments[0], '_blank', 'width=800,height=600');", url)
        handle = driver.window_handles[-1]
        browser_sessions[handle] = page_name
        print(f"✅ Opened {page_name} in a new window.")
        time.sleep(5)

    return browser_sessions


def perform_action(driver, page_name):
    """Executes actions based on the page name, skipping undefined pages."""
    driver.switch_to.window(driver.current_window_handle)
    time.sleep(5)

    try:
        if page_name == "Form Authentication":
            driver.find_element(*Loc.FormAuth.USERNAME_FIELD).send_keys(AuthConfig.FORM_AUTH_USERNAME)
            driver.find_element(*Loc.FormAuth.PASSWORD_FIELD).send_keys(AuthConfig.FORM_AUTH_PASSWORD)
            driver.find_element(*Loc.FormAuth.LOGIN_BUTTON).click()
            print("✅ Logged in via Form Authentication.")
            time.sleep(5)

        elif page_name == "Entry Ad":
            try:
                modal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Loc.EntryAd.MODAL))
                driver.find_element(*Loc.EntryAd.MODAL_CLOSE_BUTTON).click()
                print("✅ Closed Entry Ad popup.")
            except:
                print("⚠️ No Entry Ad popup found.")
            time.sleep(5)

        elif page_name == "Context Menu":
            driver.find_element(*Loc.ContextMenu.HOT_SPOT).click()
            print("✅ Right-clicked on Context Menu hotspot.")
            time.sleep(5)

        elif page_name == "Digest Authentication":
            driver.get(PAGE_URLS["digest_auth"])
            time.sleep(2)  # Allow page to load
            
            try:
                alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
                alert.send_keys(AuthConfig.DIGEST_AUTH_USERNAME)  # Send username
                alert.send_keys("\t")  # Tab to move to password field
                alert.send_keys(AuthConfig.DIGEST_AUTH_PASSWORD)  # Send password
                alert.accept()
                print("✅ Successfully authenticated via Digest Authentication.")
            except:
                print("⚠️ No authentication popup appeared or credentials failed.")
            time.sleep(5)

        elif page_name == "File Upload":
            try:
                file_input = driver.find_element(*Loc.FileUpload.FILE_INPUT)
                upload_button = driver.find_element(*Loc.FileUpload.UPLOAD_BUTTON)
                downloaded_files = os.listdir(DOWNLOADS_DIR)

                if not downloaded_files:
                    raise Exception("No files found in the download folder.")

                latest_file = max([os.path.join(DOWNLOADS_DIR, f) for f in downloaded_files], key=os.path.getctime)
                print(f"✅ Uploading file: {latest_file}")

                file_input.send_keys(latest_file)
                upload_button.click()
                print("✅ File uploaded successfully.")
            except Exception as e:
                print(f"❌ File upload failed: {e}")
            time.sleep(5)

        else:
            print(f"⚠️ No interaction logic implemented for: {page_name}")

    except Exception as e:
        print(f"❌ Error while interacting with {page_name}: {e}")
        time.sleep(5)


def execute_actions(driver, browser_sessions, user_defined_interactions):
    """Executes actions for user-specified pages, then closes all tabs/windows in the defined order."""
    processed_sessions = {}

    for handle, page_name in browser_sessions.items():
        if page_name in user_defined_interactions:
            driver.switch_to.window(handle)
            print(f"🔄 Switching to {page_name}...")
            perform_action(driver, page_name)
            processed_sessions[handle] = page_name

    print("✅ All user-defined interactions completed.")
    time.sleep(5)

    # Close only the interacted tabs/windows in the same order
    for handle, page_name in processed_sessions.items():
        driver.switch_to.window(handle)
        driver.close()
        print(f"❌ Closed {page_name}.")
        time.sleep(5)

    # Close any remaining tabs/windows that were opened but never interacted with
    for handle, page_name in browser_sessions.items():
        if handle not in processed_sessions:
            driver.switch_to.window(handle)
            driver.close()
            print(f"❌ Closed (unused) {page_name}.")
            time.sleep(5)

    # Return to base tab
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)


def main(user_defined_interactions):
    """Executes the automation process with user-defined page interactions."""
    driver = setup_driver()
    driver.get(PAGE_URLS["base"])
    print("✅ Base page loaded.")

    # Open all pages and store their handles
    browser_sessions = open_pages(driver)

    # Execute actions only for pages defined by the user
    execute_actions(driver, browser_sessions, user_defined_interactions)

    print("✅ Test Scenario Completed Successfully!")
    teardown_driver(driver)


if __name__ == "__main__":
    # User specifies which pages they want to interact with
    user_defined_interactions = ["Form Authentication", "Digest Authentication", "File Upload"]
    main(user_defined_interactions)