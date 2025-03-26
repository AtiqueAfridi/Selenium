📖 README - Selenium Automation Project
🚀 Selenium Automation Framework
📌 A powerful Selenium automation framework for dynamic web interactions.

🔹 Automates Form Authentication, File Uploads, Digest Authentication, and more!
🔹 Manages multiple tabs & windows efficiently.
🔹 Users control execution order via a Python dictionary.

📌 Features
✅ Dynamic element identification (No hardcoded selectors)
✅ Custom execution order (Users define which pages to interact with)
✅ Proper tab & window handling
✅ Automated Digest Authentication
✅ Secure file handling (Uploads recent downloads)

📁 Project Structure
bash
Copy
Edit
Selenium/
│── src/
│   ├── main.py             # Main automation script
│   ├── locators.py         # Dynamic element locators
│   ├── config.py           # Configuration settings & credentials
│   ├── utilities.py        # Setup, teardown & helper functions
│── downloads/              # Stores downloaded files
│── README.md               # Project documentation
🛠️ Installation & Setup
1️⃣ Prerequisites
✅ Python 3.x

✅ Google Chrome

✅ ChromeDriver (chromedriver.exe)

2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Configure Credentials (config.py)
python
Copy
Edit
# Update credentials in src/config.py
DIGEST_AUTH_USERNAME = "admin"
DIGEST_AUTH_PASSWORD = "admin"
🚀 Running the Automation
Run the script with user-defined execution order
bash
Copy
Edit
python -m src.main
📌 How It Works
1️⃣ Opens specific pages in new tabs/windows
2️⃣ Executes only the user-specified actions
3️⃣ Closes pages in the order of execution

📝 Example Usage
Define execution order in main.py
python
Copy
Edit
user_defined_interactions = ["Form Authentication", "Digest Authentication", "File Upload"]
main(user_defined_interactions)
📌 Contributing
🔹 Fork the repository
🔹 Create a new branch (feature/new-feature)
🔹 Submit a pull request

📄 License
📜 MIT License - Free to use & modify.

📬 Contact
📧 Email: atique@example.com
🐍 GitHub: AtiqueAfridi/Selenium

🔥 Star this repo if you found it useful! 🚀