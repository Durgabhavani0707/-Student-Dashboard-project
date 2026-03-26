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
        password="A*durgabhavani07",
        database="studentdb"
    )

# ✅ DASHBOARD API
@app.route('/dashboard/<regno>')
def dashboard(regno):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM subjects WHERE regno=%s", (regno,))
    rows = cursor.fetchall()

    # 🔥 DEFAULT ALL CATEGORIES (IMPORTANT FIX)
    categories = {
        "AUC":0,
        "HAS":0,
        "SIL":0,
        "BSC":0,
        "ESC":0,
        "PCC":0,
        "PEC":0,
        "HFC":0,
        "SDC":0,
        "PRI":0,
        "OEC":0,
        "VAC":0
    }

    # 🔥 COUNT COMPLETED FROM DB
    for r in rows:
        if r['status'] == "completed":
            cat = r['category']
            if cat in categories:
                categories[cat] += 1

    result = []

    # 🔥 ALWAYS RETURN ALL CATEGORIES
    for cat, completed in categories.items():
        total = CATEGORY_TOTALS.get(cat, 0)
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