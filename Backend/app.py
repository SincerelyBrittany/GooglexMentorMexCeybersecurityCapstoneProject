from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])
# CORS(app)  # This allows all origins (good for development)

DB = 'quiz_results.db'

@app.route('/submit', methods=['POST'])
def submit_result():
    data = request.get_json()
    email = data.get('email')
    score = data.get('score')
    missed = data.get('missed_warning')

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO results (user_email, score, missed_warning)
        VALUES (?, ?, ?)
    """, (email, score, missed))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Result saved"}), 201

@app.route('/top-mistakes', methods=['GET'])
def top_mistakes():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT missed_warning, COUNT(*) as count
        FROM results
        GROUP BY missed_warning
        ORDER BY count DESC
        LIMIT 5
    """)
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{"missed_warning": r[0], "count": r[1]} for r in rows])

if __name__ == '__main__':
    app.run(debug=True)
