from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ FIXED TOTAL SUBJECTS PER CATEGORY
CATEGORY_TOTALS = {
    "AUC":7,
    "HAS":7,
    "SIL":3,
    "BSC":8,
    "ESC":8,
    "PCC":17,
    "PEC":7,
    "HFC":4,
    "SDC":8,
    "PRI":14,
    "OEC":3,
    "VAC":5
}

# ✅ DB CONNECTION
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="A*durgabhavani07",  # your password
        database="studentdb"
    )

# ✅ DASHBOARD API
@app.route('/dashboard/<regno>')
def dashboard(regno):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM subjects WHERE regno=%s", (regno,))
    rows = cursor.fetchall()

    # ❌ NO DATA CASE
    if len(rows) == 0:
        return jsonify({
            "message": "No data found for this student"
        })

    categories = {}

    # 🔥 COUNT ONLY COMPLETED
    for r in rows:
        cat = r['category']

        if cat not in categories:
            categories[cat] = {
                "completed": 0
            }

        if r['status'] == "completed":
            categories[cat]["completed"] += 1

    result = []

    # 🔥 APPLY FIXED TOTALS
    for cat, val in categories.items():
        total = CATEGORY_TOTALS.get(cat, 0)
        completed = val["completed"]
        remaining = total - completed
        progress = int((completed / total) * 100) if total > 0 else 0

        result.append({
            "category": cat,
            "total": total,
            "completed": completed,
            "remaining": remaining,
            "progress": progress
        })

    cursor.close()
    conn.close()

    return jsonify(result)

# ✅ RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)