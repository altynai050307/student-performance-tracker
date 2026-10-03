from flask import Flask, jsonify, request

app = Flask(__name__)

# Студенттердің үлгерімін есепке алуға арналған деректер базасының симуляциясы
students_performance = [
    {"id": 1, "name": "Айша", "subject": "DevOps", "grade": 95},
    {"id": 2, "name": "Асқар", "subject": "DevOps", "grade": 88}
]

@app.route('/')
def home():
    return jsonify({"message": "Студенттердің үлгерімін есепке алу жүйесіне кош келдіңіз!"})

@app.route('/api/grades', methods=['GET'])
def get_grades():
    return jsonify({"students": students_performance, "status": "success"})

@app.route('/api/grades', methods=['POST'])
def add_grade():
    data = request.get_json()
    if not data or 'name' not in data or 'grade' not in data:
        return jsonify({"error": "Деректер толық емес!"}), 400
    
    new_student = {
        "id": len(students_performance) + 1,
        "name": data['name'],
        "subject": data.get('subject', 'Ақпараттық жүйелер'),
        "grade": data['grade']
    }
    students_performance.append(new_student)
    return jsonify(new_student), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)