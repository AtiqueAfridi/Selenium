import time
import os
import requests
from requests.auth import HTTPDigestAuth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.utilities import setup_driver, teardown_driver, DOWNLOADS_DIR
from src.locators import Loc
from src.config import AuthConfig, PAGE_URLS


def get_authenticated_cookies():
    """Sends a request to the Digest Authentication page and retrieves session cookies."""
    session = requests.Session()
    response = session.get(PAGE_URLS["digest_auth"], auth=HTTPDigestAuth(AuthConfig.DIGEST_AUTH_USERNAME, AuthConfig.DIGEST_AUTH_PASSWORD))

    if response.status_code == 200:
        print("✅ Pre-authentication successful.")
        return session.cookies.get_dict()
    else:
        print(f"❌ Failed to authenticate. Status Code: {response.status_code}")
        return None


def setup_driver_with_auth():
    """Sets up the Selenium WebDriver and injects pre-authenticated cookies."""
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get("about:blank")  # Load a blank page first

    # Retrieve authentication cookies
    cookies = get_authenticated_cookies()
    if cookies:
        driver.get(PAGE_URLS["digest_auth"])  # Navigate to the page first to set the domain
        for name, value in cookies.items():
            driver.add_cookie({"name": name, "value": value})
        print("✅ Cookies injected into Selenium session.")
    
    return driver


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
        time.sleep(3)

    # Open pages in new windows
    for page_name, url in window_pages.items():
        driver.execute_script("window.open(arguments[0], '_blank', 'width=800,height=600');", url)
        handle = driver.window_handles[-1]
        browser_sessions[handle] = page_name
        print(f"✅ Opened {page_name} in a new window.")
        time.sleep(3)

    return browser_sessions


from selenium.webdriver.common.action_chains import ActionChains

def perform_action(driver, page_name):
    """Executes actions based on the page name, skipping undefined pages."""
    driver.switch_to.window(driver.current_window_handle)
    time.sleep(3)

    try:
        if page_name == "Form Authentication":
            driver.find_element(*Loc.FormAuth.USERNAME_FIELD).send_keys(AuthConfig.FORM_AUTH_USERNAME)
            driver.find_element(*Loc.FormAuth.PASSWORD_FIELD).send_keys(AuthConfig.FORM_AUTH_PASSWORD)
            driver.find_element(*Loc.FormAuth.LOGIN_BUTTON).click()
            print("✅ Logged in via Form Authentication.")
            time.sleep(3)

        elif page_name == "Entry Ad":
            try:
                modal = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Loc.EntryAd.MODAL))
                driver.find_element(*Loc.EntryAd.MODAL_CLOSE_BUTTON).click()
                print("✅ Closed Entry Ad popup.")
            except:
                print("⚠️ No Entry Ad popup found.")
            time.sleep(3)

        elif page_name == "Context Menu":
            try:
                context_menu_element = driver.find_element(*Loc.ContextMenu.HOT_SPOT)
                actions = ActionChains(driver)
                actions.context_click(context_menu_element).perform()  # ✅ Right-click action
                print("✅ Right-clicked on Context Menu hotspot.")

                # ✅ Handle alert
                WebDriverWait(driver, 3).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                print(f"🔴 Alert Text: {alert.text}")
                alert.accept()
                print("✅ Alert dismissed.")
            except Exception as e:
                print(f"❌ Error interacting with Context Menu: {e}")

            time.sleep(3)

        elif page_name == "Digest Authentication":
            print("✅ Digest Authentication already completed via pre-authentication.")
            time.sleep(3)

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

            time.sleep(3)

        else:
            print(f"⚠️ No interaction logic implemented for: {page_name}")

    except Exception as e:
        print(f"❌ Error while interacting with {page_name}: {e}")
        time.sleep(3)


def execute_actions(driver, browser_sessions, user_defined_interactions):
    """Executes actions for user-specified pages in the exact order they were defined."""
    processed_sessions = {}

    # ✅ Loop through user-defined order instead of browser_sessions order
    for page_name in user_defined_interactions:
        # Find the handle corresponding to the page name
        handle = next((h for h, p in browser_sessions.items() if p == page_name), None)

        if handle:
            driver.switch_to.window(handle)
            print(f"🔄 Switching to {page_name}...")
            perform_action(driver, page_name)
            processed_sessions[handle] = page_name
        else:
            print(f"⚠️ Warning: {page_name} was not opened.")

    print("✅ All user-defined interactions completed.")
    time.sleep(3)

    # ✅ Ensure the user sees each tab before it closes
    for page_name in user_defined_interactions:
        handle = next((h for h, p in processed_sessions.items() if p == page_name), None)

        if handle:
            driver.switch_to.window(handle)  # ✅ Switch before closing
            print(f"👀 Bringing {page_name} to focus before closing...")
            time.sleep(2)  # ✅ Let the user see the tab before closing
            driver.close()
            print(f"❌ Closed {page_name}.")
            time.sleep(2)  # ✅ Give a moment before closing next tab

    # ✅ Close any remaining tabs/windows that were opened but never interacted with
    for handle, page_name in browser_sessions.items():
        if handle not in processed_sessions:
            driver.switch_to.window(handle)
            print(f"👀 Bringing unused {page_name} to focus before closing...")
            time.sleep(2)  # ✅ Let user see the unused tab
            driver.close()
            print(f"❌ Closed (unused) {page_name}.")
            time.sleep(2)

    # ✅ Return to base tab
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)




def main(user_defined_interactions):
    """Executes the automation process with user-defined page interactions."""
    driver = setup_driver_with_auth()  # ✅ Using pre-authentication setup
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
    user_defined_interactions = ["Entry Ad", "Digest Authentication", "Form Authentication","File Upload", "Context Menu" ]
    main(user_defined_interactions)
