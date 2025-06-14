# import pandas as pd
# import re
# from collections import Counter

# # Load your dataset
# df = pd.read_csv('phishing_emails.csv')  # Replace with your dataset path
# phishing_texts = df['email_text']  # Adjust column name as needed

# # Extract keywords from emails (very basic example)
# def extract_keywords(text):
#     words = re.findall(r'\b\w{4,}\b', text.lower())  # Words with 4+ letters
#     return words

# # Apply function to all emails
# all_words = []
# for email in phishing_texts.dropna():
#     all_words.extend(extract_keywords(email))

# # Count most common words
# common_words = Counter(all_words).most_common(20)
# print("Top phishing words:")
# for word, freq in common_words:
#     print(f"{word}: {freq}")

# # Optionally save to CSV or DB
# keywords_df = pd.DataFrame(common_words, columns=["keyword", "frequency"])
# keywords_df['is_common'] = keywords_df['frequency'] > 10
# keywords_df.to_csv("top_phishing_words.csv", index=False)


# import pandas as pd
# import re
# import sqlite3
# from collections import Counter

# df = pd.read_csv('phishing_emails.csv')  # Replace with your actual file
# phishing_texts = df['body']  # Adjust column name if needed

# def extract_keywords(text):
#     return re.findall(r'\b\w{4,}\b', text.lower())

# all_words = []
# for email in phishing_texts.dropna():
#     all_words.extend(extract_keywords(email))

# common_words = Counter(all_words).most_common(20)
# keywords_df = pd.DataFrame(common_words, columns=["keyword", "frequency"])
# keywords_df['is_common'] = keywords_df['frequency'] > 10

# conn = sqlite3.connect('quiz_results.db')
# cursor = conn.cursor()
# cursor.execute("DELETE FROM phishing_patterns")
# for _, row in keywords_df.iterrows():
#     cursor.execute("""
#         INSERT INTO phishing_patterns (keyword, frequency, is_common)
#         VALUES (?, ?, ?)
#     """, (row['keyword'], row['frequency'], row['is_common']))
# conn.commit()
# conn.close()


# import pandas as pd
# import re
# import sqlite3
# from collections import Counter
# from nltk.corpus import stopwords
# import nltk

# nltk.download('stopwords')
# stop_words = set(stopwords.words('english'))

# df = pd.read_csv('Phishing_Email.csv')
# phishing_texts = df['Email Text']  # <-- adjust this to match actual column

# def extract_keywords(text):
#     words = re.findall(r'\b\w{4,}\b', text.lower())
#     return [word for word in words if word not in stop_words and word.isalpha()]

# all_words = []
# for email in phishing_texts.dropna():
#     all_words.extend(extract_keywords(email))

# common_words = Counter(all_words).most_common(20)
# keywords_df = pd.DataFrame(common_words, columns=["keyword", "frequency"])
# keywords_df['is_common'] = keywords_df['frequency'] > 10

# conn = sqlite3.connect('quiz_results.db')
# cursor = conn.cursor()
# cursor.execute("DELETE FROM phishing_patterns")
# for _, row in keywords_df.iterrows():
#     cursor.execute("""
#         INSERT INTO phishing_patterns (keyword, frequency, is_common)
#         VALUES (?, ?, ?)
#     """, (row['keyword'], row['frequency'], row['is_common']))
# conn.commit()
# conn.close()

# print("✅ Phishing keywords saved to DB.")



# import pandas as pd
# import re
# import sqlite3
# from collections import Counter
# from nltk.corpus import stopwords
# import nltk

# nltk.download('stopwords')
# stop_words = set(stopwords.words('english'))

# # Load only phishing emails
# df = pd.read_csv('Phishing_Email.csv')
# phishing_texts = df[df['Email Type'] == 'Phishing Email']['Email Text']

# def extract_keywords(text):
#     words = re.findall(r'\b\w{4,}\b', text.lower())
#     return [word for word in words if word not in stop_words and word.isalpha()]

# all_words = []
# for email in phishing_texts.dropna():
#     all_words.extend(extract_keywords(email))

# common_words = Counter(all_words).most_common(20)
# keywords_df = pd.DataFrame(common_words, columns=["keyword", "frequency"])
# keywords_df['is_common'] = keywords_df['frequency'] > 10

# conn = sqlite3.connect('quiz_results.db')
# cursor = conn.cursor()
# cursor.execute("DELETE FROM phishing_patterns")
# for _, row in keywords_df.iterrows():
#     cursor.execute("""
#         INSERT INTO phishing_patterns (keyword, frequency, is_common)
#         VALUES (?, ?, ?)
#     """, (row['keyword'], row['frequency'], row['is_common']))
# conn.commit()
# conn.close()

# print("✅ Phishing keywords saved to DB.")


import pandas as pd
import re
import sqlite3
from collections import Counter

# Load dataset
df = pd.read_csv('Phishing_Email.csv')  # ✅ matches your new file
phishing_texts = df['Email Text']       # ✅ correct column name

def extract_keywords(text):
    return re.findall(r'\b\w{4,}\b', text.lower())  # extract 4+ letter words

# Extract keywords from all emails
all_words = []
for email in phishing_texts.dropna():
    all_words.extend(extract_keywords(email))

# Count top 20 keywords
common_words = Counter(all_words).most_common(100)
keywords_df = pd.DataFrame(common_words, columns=["keyword", "frequency"])
keywords_df['is_common'] = keywords_df['frequency'] >= 5  # or >= 15

# keywords_df['is_common'] = keywords_df['frequency'] > 10


# Insert into SQLite database
conn = sqlite3.connect('quiz_results.db')
cursor = conn.cursor()
cursor.execute("DELETE FROM phishing_patterns")  # clear existing
for _, row in keywords_df.iterrows():
    cursor.execute("""
        INSERT INTO phishing_patterns (keyword, frequency, is_common)
        VALUES (?, ?, ?)
    """, (row['keyword'], row['frequency'], row['is_common']))
conn.commit()
conn.close()
