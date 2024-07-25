from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST')
    )
    return conn

@app.route('/')
def home():
    return 'Flask API is running!'

@app.route('/testcases', methods=['GET'])
def get_testcases():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, test_case_name, description, status, estimate_time, module, priority, last_updated FROM testcases ORDER BY id ASC;')
    testcases = cur.fetchall()
    cur.close()
    conn.close()
    
    testcases_list = [
        {'id': tc[0], 'test_case_name': tc[1], 'description': tc[2], 'status': tc[3], 'estimate_time': tc[4], 'module': tc[5], 'priority': tc[6], 'last_updated': tc[7]}
        for tc in testcases
    ]
    
    return jsonify(testcases_list)

@app.route('/testcases/<int:id>', methods=['PUT'])
def update_testcase(id):
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE testcases SET test_case_name = %s, description = %s, status = %s, estimate_time = %s, module = %s, priority = %s, last_updated = %s WHERE id = %s',
                (data['test_case_name'], data['description'], data['status'], data['estimate_time'], data['module'], data['priority'], data['last_updated'], id))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204

if __name__ == '__main__':
    app.run(port=5000)
