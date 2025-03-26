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


# import time
# import random
# import os
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from src.utilities import setup_driver, teardown_driver, DOWNLOADS_DIR
# from src.locators import Loc
# from src.config import AuthConfig, PAGE_URLS



# def open_pages_in_tabs(driver):
#     """Opens specific pages in new tabs and stores their handles."""
#     print("Opening pages in new tabs...")
#     tab_pages = {
#         "Form Authentication": PAGE_URLS["login"],
#         "Entry Ad": PAGE_URLS["entry_ad"],
#         "Context Menu": PAGE_URLS["context_menu"]
#     }

#     tab_handles = []
#     for page_name, url in tab_pages.items():
#         driver.execute_script("window.open(arguments[0], '_blank');", url)
#         tab_handles.append((driver.window_handles[-1], page_name))
#         print(f"✅ Opened {page_name} in a new tab.")
#         time.sleep(2)

#     return tab_handles

# def open_pages_in_new_windows(driver):
#     """Opens specific pages in new windows and stores their handles."""
#     print("Opening pages in new windows...")
#     window_pages = {
#         "Digest Authentication": PAGE_URLS["digest_auth"],
#         "File Upload": PAGE_URLS["file_upload"]
#     }

#     window_handles = []
#     for page_name, url in window_pages.items():
#         driver.execute_script("window.open(arguments[0], '_blank', 'width=800,height=600');", url)
#         window_handles.append((driver.window_handles[-1], page_name))
#         print(f"✅ Opened {page_name} in a new window.")
#         time.sleep(2)

#     return window_handles

# def wait_for_all_tabs_to_open(driver, expected_count):
#     """Waits until all tabs/windows are fully opened before proceeding."""
#     timeout = 10  # Maximum wait time
#     start_time = time.time()

#     while len(driver.window_handles) < expected_count:
#         if time.time() - start_time > timeout:
#             print("⚠️ Timeout: Not all tabs/windows opened.")
#             break
#         time.sleep(1)

#     print(f"✅ All {len(driver.window_handles) - 1} pages opened successfully.")

# def perform_action(driver, page_name):
#     """Executes the relevant action for each page."""
#     driver.switch_to.window(driver.current_window_handle)  # Ensure focus
#     time.sleep(1)  # Allow page elements to load

#     if page_name == "Form Authentication":
#         driver.find_element(*Loc.FormAuth.USERNAME_FIELD).send_keys(AuthConfig.FORM_AUTH_USERNAME)
#         driver.find_element(*Loc.FormAuth.PASSWORD_FIELD).send_keys(AuthConfig.FORM_AUTH_PASSWORD)
#         driver.find_element(*Loc.FormAuth.LOGIN_BUTTON).click()
#         print("✅ Logged in via Form Authentication.")

#     elif page_name == "Entry Ad":
#         try:
#             modal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Loc.EntryAd.MODAL))
#             driver.find_element(*Loc.EntryAd.MODAL_CLOSE_BUTTON).click()
#             print("✅ Closed Entry Ad popup.")
#         except:
#             print("⚠️ No Entry Ad popup found.")

#     elif page_name == "Context Menu":
#         driver.find_element(*Loc.ContextMenu.HOT_SPOT).click()
#         print("✅ Right-clicked on Context Menu hotspot.")

#     if page_name == "Digest Authentication":
#         driver.get(PAGE_URLS["digest_auth"])

#         try:
#             # Handle authentication popup
#             alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
#             alert.send_keys(AuthConfig.DIGEST_AUTH_USERNAME + Keys.TAB + AuthConfig.DIGEST_AUTH_PASSWORD)
#             alert.accept()
#             print("✅ Successfully authenticated via Digest Authentication.")
#         except:
#             print("⚠️ No authentication popup appeared.")

#     # elif page_name == "Digest Authentication":
#     #     digest_auth_url = f"https://{AuthConfig.DIGEST_AUTH_CREDENTIALS}@{PAGE_URLS['digest_auth']}"
#     #     driver.get(digest_auth_url)  # ✅ Now passing credentials in URL
#     #     print("✅ Successfully authenticated via Digest Authentication.")
        

#     elif page_name == "File Upload":
#         try:
#             file_input = driver.find_element(*Loc.FileUpload.FILE_INPUT)
#             upload_button = driver.find_element(*Loc.FileUpload.UPLOAD_BUTTON)

#             # Fetch any available file from the downloads folder
#             downloaded_files = os.listdir(DOWNLOADS_DIR)
#             if not downloaded_files:
#                 raise Exception("No files found in the download folder.")
            
#             latest_file = max([os.path.join(DOWNLOADS_DIR, f) for f in downloaded_files], key=os.path.getctime)
#             print(f"✅ Uploading file: {latest_file}")

#             file_input.send_keys(latest_file)
#             upload_button.click()
#             print("✅ File uploaded successfully.")
#         except Exception as e:
#             print(f"❌ File upload failed: {e}")

# def switch_and_execute(driver, all_handles, random_execution):
#     """Switches to each tab/window and executes the relevant action."""
#     if random_execution:
#         random.shuffle(all_handles)

#     for handle, page_name in all_handles:
#         if handle not in driver.window_handles:
#             print(f"⚠️ Skipping {page_name}: Window already closed.")
#             continue
        
#         driver.switch_to.window(handle)
#         print(f"🔄 Switching to {page_name}...")
#         perform_action(driver, page_name)

#     for handle, page_name in all_handles:
#         if handle in driver.window_handles:
#             driver.switch_to.window(handle)
#             driver.close()
#             print(f"❌ Closed {page_name}.")

#     driver.switch_to.window(driver.window_handles[0])  # Return to base tab

# def main(random_execution=True):
#     """Executes the Selenium automation test with controlled tab/window handling."""
#     driver = setup_driver()
#     driver.get(PAGE_URLS["base"])
#     print("✅ Base page loaded.")

#     # Open tabs and windows
#     tab_handles = open_pages_in_tabs(driver)
#     window_handles = open_pages_in_new_windows(driver)

#     # Wait for all tabs/windows to fully open before executing tasks
#     wait_for_all_tabs_to_open(driver, len(tab_handles) + len(window_handles) + 1)

#     # Combine handles and execute tasks
#     all_handles = tab_handles + window_handles
#     switch_and_execute(driver, all_handles, random_execution)

#     print("✅ Test Scenario Completed Successfully!")
#     teardown_driver(driver)

# if __name__ == "__main__":
#     random_execution = False  # Change to False for sequential execution
#     main(random_execution)
