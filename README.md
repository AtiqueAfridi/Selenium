# **🚀 Selenium Automation Project**  

## **📌 Overview**  
This project automates web interactions using **Selenium WebDriver**. The automation handles **form authentication, file uploads, entry ad pop-ups, context menus, and digest authentication**, ensuring a robust and scalable testing framework.  

---

## **🛠 Features**  
✅ Opens web pages in **new tabs or new windows** based on configuration.  
✅ **User-defined execution** — only interacts with specified pages.  
✅ Uses a **Python dictionary** to track and close browser sessions properly.  
✅ Handles **Digest Authentication** using credentials.  
✅ Manages **file uploads** dynamically from a designated folder.  
✅ Implements **intelligent tab/window closing** logic.  
✅ Ensures **smooth session transitions** and execution order control.  

---

## **📂 Project Structure**  
```
Selenium/
│── src/
│   ├── main.py             # Main script to execute the automation
│   ├── locators.py         # Stores all element locators
│   ├── config.py           # Configuration settings & Credentials
│   ├── utilities.py        # Helper functions for setup & teardown
│   ├── authentication_test.py  # Authentication handling
│── downloads/              # Folder where downloaded files are stored
│── README.md               # Project documentation
│── requirements.txt        # Dependencies list
│── .gitignore              # Ignored files (e.g., logs, venv)
```

---

## **⚙️ Setup & Installation**  

### **🔹 Prerequisites**  
1️⃣ **Install Python (≥3.8)** - [Download Here](https://www.python.org/downloads/)  
2️⃣ **Install Google Chrome** (latest version)  
3️⃣ **Download ChromeDriver** and place it in the project directory  
   - [Get ChromeDriver](https://sites.google.com/chromium.org/driver/)  

### **🔹 Install Required Packages**  
Run the following command to install dependencies:  
```bash
pip install -r requirements.txt
```

---

## **🚀 Running the Automation**  
To execute the test automation, run:  
```bash
python -m src.main
```
If you want to specify **which pages to interact with**, modify the list in `main.py`:  
```python
user_defined_interactions = ["Form Authentication", "Digest Authentication", "File Upload"]
main(user_defined_interactions)
```

---

## **📌 How It Works**  
1️⃣ **Opens the base page** and keeps it active.  
2️⃣ **Opens specified pages** in new tabs or windows.  
3️⃣ **Executes user-defined actions** on selected pages.  
4️⃣ **Handles authentication, pop-ups, file uploads, and interactions.**  
5️⃣ **Closes pages in the correct sequence** (based on user interaction).  

---

## **🛠 Supported Scenarios**  
| Feature                 | Status   | Description |
|-------------------------|---------|-------------|
| Form Authentication     | ✅ Done | Logs in using predefined credentials |
| Entry Ad Handling       | ✅ Done | Detects and closes modal pop-ups |
| Context Menu            | ✅ Done | Right-clicks on the context menu |
| Digest Authentication   | ✅ Done | Automatically enters credentials |
| File Upload             | ✅ Done | Uploads a file from the `downloads/` folder |
| File Download Handling  | ⏳ Skipped | Not implemented due to server issue |

---

## **📡 Git Workflow (Contributing)**
### **🔄 Pushing Changes to Remote Repository**
```bash
git add .
git commit -m "Updated automation workflow"
git push origin main
```

### **🔀 Creating a New Branch**
```bash
git checkout -b feature-new-task
git push origin feature-new-task
```

### **📌 Merging Branches**
```bash
git checkout main
git merge feature-new-task
git push origin main
```

---

## **📜 License**
This project is **open-source** and available under the **MIT License**.  

---

## **📞 Need Help?**
📧 Email: `atiqueafridi10@gmail.com`  
 

---

🔥 **Happy Testing!** 🚀
