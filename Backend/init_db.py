# import sqlite3

# conn = sqlite3.connect("quiz_results.db")
# cursor = conn.cursor()

# # Create the results table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS results (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_email TEXT,
#     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
#     score INTEGER,
#     missed_warning TEXT
# )
# """)

# # Optional: Create phishing_patterns table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS phishing_patterns (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     keyword TEXT,
#     frequency INTEGER,
#     is_common BOOLEAN
# )
# """)

# conn.commit()
# conn.close()
# print("✅ Database initialized!")

import sqlite3
conn = sqlite3.connect("quiz_results.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    score INTEGER,
    missed_warning TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS phishing_patterns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT NOT NULL,
    frequency INTEGER,
    is_common BOOLEAN
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT,
    option_b TEXT,
    correct_option TEXT,
    missed_warning TEXT
)
""")

conn.commit()
conn.close()
