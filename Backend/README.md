✅ Step 1: Install Flask
Run this in your terminal:

pip install flask

If you’re using Python 3 and that doesn't work, try:

pip3 install flask

🛠 Optional: Create a Virtual Environment (Recommended)
To keep your project clean:

python -m venv venv
source venv/bin/activate   # On macOS/Linux
# OR
venv\Scripts\activate      # On Windows

pip install flask

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

✅ Step 2: Re-run Your App
Once Flask is installed, try:

python app.py
python3 app.py


 Bonus: See the data inside the database
You can inspect the database using the built-in CLI:

bash
Copy
Edit
sqlite3 quiz_results.db
Then run:

sql
Copy
Edit
SELECT * FROM results;
To quit:

sql
Copy
Edit
.quit


pip install flask flask-cors pandas
pip freeze > requirements.txt