# from flask import Flask, request, jsonify
# import sqlite3
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app, origins=["http://localhost:5173"])
# # CORS(app)  # This allows all origins (good for development)

# DB = 'quiz_results.db'

# @app.route('/submit', methods=['POST'])
# def submit_result():
#     data = request.get_json()
#     email = data.get('email')
#     score = data.get('score')
#     missed = data.get('missed_warning')

#     conn = sqlite3.connect(DB)
#     cursor = conn.cursor()
#     cursor.execute("""
#         INSERT INTO results (user_email, score, missed_warning)
#         VALUES (?, ?, ?)
#     """, (email, score, missed))
#     conn.commit()
#     conn.close()
    
#     return jsonify({"message": "Result saved"}), 201

# @app.route('/top-mistakes', methods=['GET'])
# def top_mistakes():
#     conn = sqlite3.connect(DB)
#     cursor = conn.cursor()
#     cursor.execute("""
#         SELECT missed_warning, COUNT(*) as count
#         FROM results
#         GROUP BY missed_warning
#         ORDER BY count DESC
#         LIMIT 5
#     """)
#     rows = cursor.fetchall()
#     conn.close()
#     return jsonify([{"missed_warning": r[0], "count": r[1]} for r in rows])

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
DB = 'quiz_results.db'

@app.route('/submit', methods=['POST'])
def submit_result():
    data = request.get_json()
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO results (user_email, score, missed_warning)
        VALUES (?, ?, ?)
    """, (data['email'], data['score'], data['missed_warning']))
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

# @app.route('/phishing-patterns', methods=['GET'])
# def get_keywords():
#     conn = sqlite3.connect(DB)
#     cursor = conn.cursor()
#     cursor.execute("""
#         SELECT keyword, frequency, is_common
#         FROM phishing_patterns
#         ORDER BY frequency DESC
#         LIMIT 20
#     """)
#     rows = cursor.fetchall()
#     conn.close()
#     return jsonify([
#         {"keyword": r[0], "frequency": r[1], "is_common": bool(r[2])}
#         for r in rows
#     ])

@app.route('/top-keywords', methods=['GET'])
def top_keywords():
    import sqlite3
    from flask import request, jsonify

    filter_type = request.args.get('filter', 'all')  # 'common', 'uncommon', or 'all'
    query = "SELECT keyword, frequency, is_common FROM phishing_patterns"

    if filter_type == 'common':
        query += " WHERE is_common = 1"
    elif filter_type == 'uncommon':
        query += " WHERE is_common = 0"

    query += " ORDER BY frequency DESC LIMIT 20"

    conn = sqlite3.connect('quiz_results.db')
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    keywords = [
        {"keyword": row[0], "frequency": row[1], "is_common": bool(row[2])}
        for row in rows
    ]
    return jsonify(keywords)

    
@app.route('/questions', methods=['GET'])
def get_questions():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, question, option_a, option_b, correct_option, missed_warning
        FROM questions
    """)
    rows = cursor.fetchall()
    conn.close()

    questions = [
        {
            "id": row[0],
            "question": row[1],
            "options": {
                "option_a": row[2],
                "option_b": row[3]
            },
            "correct": row[4],
            "missed_warning": row[5]
        } for row in rows
    ]
    return jsonify(questions)

@app.route('/add-question', methods=['POST'])
def add_question():
    data = request.get_json()
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO questions (question, option_a, option_b, correct_option, missed_warning)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data['question'],
        data['option_a'],
        data['option_b'],
        data['correct_option'],
        data['missed_warning']
    ))
    conn.commit()
    conn.close()
    return jsonify({"message": "Question added successfully"}), 201

@app.route('/check-keyword', methods=['GET'])
def check_keyword():
    from flask import request, jsonify

    keyword = request.args.get('q', '').lower().strip()

    if not keyword or len(keyword) < 2:
        return jsonify({'error': 'Invalid keyword'}), 400

    conn = sqlite3.connect('quiz_results.db')
    cursor = conn.cursor()
    cursor.execute("SELECT frequency, is_common FROM phishing_patterns WHERE keyword = ?", (keyword,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({
            'keyword': keyword,
            'frequency': row[0],
            'is_common': bool(row[1])
        })
    else:
        return jsonify({'keyword': keyword, 'found': False})
    
if __name__ == '__main__':
    app.run(debug=True)
