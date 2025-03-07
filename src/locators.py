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

class FormAuthPageLocators:
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'flash success')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'flash error')]")

class FileDownloadPageLocators:
    BILLIE_JPG_LINK = (By.XPATH, "//a[text()='billie.jpg']")

class FileUploadPageLocators:
    FILE_INPUT = (By.ID, "file-upload")  # Input field to upload a file
    UPLOAD_BUTTON = (By.ID, "file-submit")  # Button to submit the upload
    UPLOAD_SUCCESS_TEXT = (By.TAG_NAME, "h3")  # Text displayed after upload

class Loc:
    AddRemove = AddRemoveElementsPageLocators
    Checkboxes = CheckboxesPageLocators
    ContextMenu = ContextMenuPageLocators
    Dropdown = DropdownPageLocators