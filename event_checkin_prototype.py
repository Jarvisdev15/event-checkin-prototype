from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
checkins = {}

@app.post("/check-in")
def check_in():
    data = request.get_json(silent=True) or {}
    student_id = data.get("student_id", "").strip()

    if not student_id:
        return jsonify(error="student_id is required"), 400

    if student_id in checkins:
        return jsonify(status="already_checked_in"), 409

    checkins[student_id] = {
        "checked_in_at": datetime.utcnow().isoformat() + "Z"
    }

    return jsonify(status="checked_in"), 201
