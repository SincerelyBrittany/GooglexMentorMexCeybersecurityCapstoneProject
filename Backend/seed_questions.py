import sqlite3

questions = [
    {
        "question": "Which subject line is most likely from a phishing email?",
        "option_a": "Reminder: Your invoice is due tomorrow",
        "option_b": "Account Suspension Notice: Act Immediately!",
        "correct": "option_b",
        "missed": "Didn’t recognize fear-based urgency"
    },
    {
        "question": "You get an email from 'micros0ft.com'. What's the red flag?",
        "option_a": "The spelling of the domain",
        "option_b": "It says it's from Microsoft",
        "correct": "option_a",
        "missed": "Didn’t spot domain typo"
    },
    {
        "question": "The email claims you won a gift card. What’s your first step?",
        "option_a": "Click the link to claim it",
        "option_b": "Verify sender and legitimacy first",
        "correct": "option_b",
        "missed": "Clicked prize without verifying"
    },
    {
        "question": "Which attachment should raise suspicion?",
        "option_a": "invoice.pdf",
        "option_b": "invoice.exe",
        "correct": "option_b",
        "missed": "Didn’t recognize risky file type"
    },
    {
        "question": "Which greeting is a red flag in business email?",
        "option_a": "Hi John",
        "option_b": "Dear Valued Customer",
        "correct": "option_b",
        "missed": "Didn’t notice generic greeting"
    },
    {
        "question": "What should you check in a link before clicking?",
        "option_a": "If it loads fast",
        "option_b": "If it matches the real domain",
        "correct": "option_b",
        "missed": "Didn’t validate domain"
    },
    {
        "question": "You receive a message saying 'You've been hacked!' What’s the likely goal?",
        "option_a": "Encourage password change",
        "option_b": "Scare you into clicking malicious links",
        "correct": "option_b",
        "missed": "Fell for scare tactic"
    },
    {
        "question": "What does a sense of urgency in a message often indicate?",
        "option_a": "Great customer service",
        "option_b": "Phishing or social engineering",
        "correct": "option_b",
        "missed": "Didn’t question urgency"
    },
    {
        "question": "Why is 'Click here to avoid suspension' suspicious?",
        "option_a": "It's too long",
        "option_b": "It's coercive and uses fear",
        "correct": "option_b",
        "missed": "Didn’t spot fear-based language"
    },
    {
        "question": "Which domain is safest?",
        "option_a": "accounts.google.verify-now.com",
        "option_b": "accounts.google.com",
        "correct": "option_b",
        "missed": "Didn’t spot subdomain trick"
    },
    {
        "question": "What does HTTPS in a URL mean?",
        "option_a": "Site is trustworthy",
        "option_b": "Connection is encrypted",
        "correct": "option_b",
        "missed": "Misunderstood HTTPS meaning"
    },
    {
        "question": "Which email structure is typical of phishing?",
        "option_a": "Clear grammar and formatting",
        "option_b": "Typos, poor formatting, vague language",
        "correct": "option_b",
        "missed": "Ignored sloppy email structure"
    },
    {
        "question": "You get an unexpected DocuSign request. What’s best?",
        "option_a": "Open it immediately",
        "option_b": "Verify with sender directly",
        "correct": "option_b",
        "missed": "Didn’t verify DocuSign request"
    },
    {
        "question": "You see a link like bit.ly/23423 in a message. What’s a concern?",
        "option_a": "It’s shortened and could hide destination",
        "option_b": "It's ugly",
        "correct": "option_a",
        "missed": "Didn’t recognize link obfuscation"
    },
    {
        "question": "Why would a file named 'Invoice.pdf.exe' be dangerous?",
        "option_a": "It’s too large",
        "option_b": "It pretends to be a PDF but is an executable",
        "correct": "option_b",
        "missed": "Missed disguised file extension"
    },
    {
        "question": "The sender address is: `amazon-support@orders.biz`. What’s wrong?",
        "option_a": "Amazon never uses that domain",
        "option_b": "It includes 'support'",
        "correct": "option_a",
        "missed": "Didn’t verify real Amazon email"
    },
    {
        "question": "Which email content is suspicious?",
        "option_a": "Invoice reminder from your boss",
        "option_b": "Invoice from someone you don’t know",
        "correct": "option_b",
        "missed": "Opened unknown invoice"
    },
    {
        "question": "Why might a sense of urgency + reward be suspicious?",
        "option_a": "It motivates quick action",
        "option_b": "Classic social engineering combo",
        "correct": "option_b",
        "missed": "Didn’t spot manipulation combo"
    },
    {
        "question": "You see a prompt to 'login with your credentials to view a document'. What should you do?",
        "option_a": "Check the domain before entering anything",
        "option_b": "Log in immediately",
        "correct": "option_a",
        "missed": "Didn’t validate domain first"
    },
    {
        "question": "Which of these is a phishing tactic?",
        "option_a": "Email signature with contact info",
        "option_b": "Faked branding to look legitimate",
        "correct": "option_b",
        "missed": "Didn’t recognize faked branding"
    }
]

conn = sqlite3.connect("quiz_results.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM questions")

for q in questions:
    cursor.execute("""
        INSERT INTO questions (question, option_a, option_b, correct_option, missed_warning)
        VALUES (?, ?, ?, ?, ?)
    """, (q["question"], q["option_a"], q["option_b"], q["correct"], q["missed"]))

conn.commit()
conn.close()
print("✅ Questions seeded.")
