# 🛡️ PhishShield Backend

This is the backend for **PhishShield**, a cybersecurity awareness app that educates users on phishing attacks through real-world simulations and keyword analysis. The backend is built with **Flask** and uses **SQLite** for lightweight local data storage.

---

## 🚀 Getting Started

### 1. Clone the repository and navigate to the backend

```bash
git clone https://github.com/yourusername/phishshield.git
cd phishshield/backend
```

### 2. Set Up Your Python Environment
```python3 -m venv venv```
```source venv/bin/activate```  # On Windows: venv\Scripts\activate


### 3. Install Dependencies

All required packages are listed in requirements.txt. Install them with:

```pip install -r requirements.txt```
If you're missing requirements.txt, you can generate it after setting up:

```pip freeze > requirements.txt```


### Seed the Database (Quiz Questions)

```python seed_questions.py```

### Run the Phishing Keyword Analysis

```python phishing_analysis.py```

This script:
- Loads phishing email text from Phishing_Email.csv
- Extracts and ranks keywords
- Saves the top keywords to the phishing_patterns table in quiz_results.db
- You can customize the dataset path or minimum keyword frequency inside the script.

### Start the Flask Server

```python app.py   ```

The app will run on http://127.0.0.1:5000

###  API Endpoints

GET /questions: Returns all quiz questions (randomizable on the frontend)

POST /submit: Accepts quiz results (email, score, missed red flags)

GET /top-keywords: Returns phishing keywords and their frequency

GET /top-keywords/common: Returns only common phishing keywords

GET /top-keywords/uncommon: Returns uncommon keywords (if any)

### Notes
Your DB (quiz_results.db) is lightweight and local. To reset, delete the file and re-run the seeding script.

Make sure Phishing_Email.csv is formatted with a column like "Email Text" or "body" for analysis.

Adjust phishing_analysis.py if you switch to a different dataset or schema.

### Example Workflow

``source venv/bin/activate``
``pip install -r requirements.txt``
``python seed_questions.py``
``python phishing_analysis.py``
``python app.py``