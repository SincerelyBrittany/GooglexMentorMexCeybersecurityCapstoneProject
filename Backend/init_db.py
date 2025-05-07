import sqlite3

conn = sqlite3.connect("quiz_results.db")
cursor = conn.cursor()

# Create the results table
cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    score INTEGER,
    missed_warning TEXT
)
""")

# Optional: Create phishing_patterns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS phishing_patterns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT,
    frequency INTEGER,
    is_common BOOLEAN
)
""")

conn.commit()
conn.close()
print("✅ Database initialized!")
