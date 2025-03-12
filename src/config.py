# Configuration file for storing credentials and other settings
# src/config.py

BASE_URL = "https://the-internet.herokuapp.com"
BASIC_AUTH_CREDENTIALS = "admin:admin"
DIGEST_AUTH_CREDENTIALS = "admin:admin"

BASIC_AUTH_URL = f"https://{BASIC_AUTH_CREDENTIALS}@{BASE_URL}/basic_auth"
DIGEST_AUTH_URL = f"https://{DIGEST_AUTH_CREDENTIALS}@{BASE_URL}/digest_auth"

PAGE_URLS = {
    "base": BASE_URL,
    "login": f"{BASE_URL}/login",  # ✅ Fixed extra "/"
    "add_remove_elements": f"{BASE_URL}/add_remove_elements",
    "checkboxes": f"{BASE_URL}/checkboxes",
    "context_menu": f"{BASE_URL}/context_menu",
    "drag_and_drop": f"{BASE_URL}/drag_and_drop",
    "dropdown": f"{BASE_URL}/dropdown",
    "file_download": f"{BASE_URL}/download",
    "file_upload": f"{BASE_URL}/upload",
    "entry_ad": f"{BASE_URL}/entry_ad",
    "forgot_password": f"{BASE_URL}/forgot_password",
}

class AuthConfig:
    FORM_AUTH_USERNAME = "tomsmith"
    FORM_AUTH_PASSWORD = "SuperSecretPassword!"
