from selenium.webdriver.common.by import By

class AddRemoveElementsPageLocators:
    ADD_BUTTON = (By.XPATH, "//button[text()= 'Add Element']")
    DELETE_BUTTON_XPATH = (By.XPATH, "//button[text() = 'Delete']")
    DELETE_BUTTON_CLASS = (By.CLASS_NAME, "added-manually")

class CheckboxesPageLocators:
    CHECKBOX_1 = (By.XPATH, "//form[@id='checkboxes']/input[1]")
    CHECKBOX_2 = (By.XPATH, "//form[@id='checkboxes']/input[2]")

class ContextMenuPageLocators:
    HOT_SPOT = (By.ID, "hot-spot")

class DragAndDropPageLocators:
    SOURCE = (By.ID, "column-a")
    TARGET = (By.ID, "column-b")

class DropdownPageLocators:
    DROPDOWN = (By.ID, "dropdown")

class BasicAuthPageLocators:
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='example']/p")

class DigestAuthPageLocators:
    SUCCESS_MESSAGE = (By.TAG_NAME, "p")
    NAV_LINK = (By.LINK_TEXT, "Digest Authentication")  # Added Locator

class FormAuthPageLocators:
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'flash success')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'flash error')]")

class FileDownloadPageLocators:
    BILLIE_JPG_LINK = (By.XPATH, "//a[text()='billie.jpg']")
    FILE_LINKS = (By.XPATH, "//div[@class='example']//a[contains(text(), 'Download')]")  # Selects all file links
    NAV_LINK = (By.LINK_TEXT, "File Download")  # Added Locator

class FileUploadPageLocators:
    FILE_INPUT = (By.ID, "file-upload")  # Input field to upload a file
    UPLOAD_BUTTON = (By.ID, "file-submit")  # Button to submit the upload
    UPLOAD_SUCCESS_TEXT = (By.TAG_NAME, "h3")  # Text displayed after upload
    NAV_LINK = (By.LINK_TEXT, "File Upload")  # Added Locator
    
class EntryAdPageLocators:
    """Locators for Entry Ad Page."""
    MODAL = (By.ID, "modal")  # The popup modal
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[@class='modal-footer']/p")

class PopupLocators:
    """Locators for handling popups (Save Password & Change Password)."""
    SAVE_PASSWORD_POPUP = (By.XPATH, "//div[contains(text(),'Save Password')]")
    NEVER_SAVE_BUTTON = (By.XPATH, "//button[text()='Never']")
    CHANGE_PASSWORD_WARNING = (By.XPATH, "//button[text()='OK']")  # Locator for Password Change Warning

# Ensure `Loc` includes all page locators

class Loc:
    AddRemove = AddRemoveElementsPageLocators
    Checkboxes = CheckboxesPageLocators
    ContextMenu = ContextMenuPageLocators
    Dropdown = DropdownPageLocators
    Dropdown = DropdownPageLocators
    FileUpload = FileUploadPageLocators
    FormAuth = FormAuthPageLocators
    EntryAd = EntryAdPageLocators
    Popup = PopupLocators
    DigestAuth = DigestAuthPageLocators  # Added Digest Authentication
    FileDownload = FileDownloadPageLocators  # Added File Download
