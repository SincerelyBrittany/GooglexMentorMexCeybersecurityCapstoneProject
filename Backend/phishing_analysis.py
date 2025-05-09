import pandas as pd
import re
from collections import Counter

# Load your dataset
df = pd.read_csv('phishing_emails.csv')  # Replace with your dataset path
phishing_texts = df['email_text']  # Adjust column name as needed

# Extract keywords from emails (very basic example)
def extract_keywords(text):
    words = re.findall(r'\b\w{4,}\b', text.lower())  # Words with 4+ letters
    return words

# Apply function to all emails
all_words = []
for email in phishing_texts.dropna():
    all_words.extend(extract_keywords(email))

# Count most common words
common_words = Counter(all_words).most_common(20)
print("Top phishing words:")
for word, freq in common_words:
    print(f"{word}: {freq}")

# Optionally save to CSV or DB
keywords_df = pd.DataFrame(common_words, columns=["keyword", "frequency"])
keywords_df['is_common'] = keywords_df['frequency'] > 10
keywords_df.to_csv("top_phishing_words.csv", index=False)
