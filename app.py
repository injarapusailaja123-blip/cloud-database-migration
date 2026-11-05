from flask import Flask, jsonify
import sqlite3, os

app = Flask(__name__)
# Codtech Task 4 - Cloud Database Migration
# Name: Injarapu Sailaja | ID: CITS9613

# STEP 1: LOCAL DATABASE (Source)
def init_local():
    conn = sqlite3.connect('local.db')
    conn.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, course TEXT)')
    conn.execute("INSERT OR IGNORE INTO students VALUES (1, 'Sailaja', 'Cloud Computing')")
    conn.execute("INSERT OR IGNORE INTO students VALUES (2, 'Priya', 'Python')")
    conn.execute("INSERT OR IGNORE INTO students VALUES (3, 'Ram', 'AWS')")
    conn.commit(); conn.close()

# STEP 2: MIGRATION - Local -> Cloud
def migrate():
    init_local()
    # Local nunchi data teesukovadam
    local = sqlite3.connect('local.db')
    data = local.execute('SELECT * FROM students').fetchall()
    local.close()
    # Cloud DB lo ki vesadam (RDS lanti Cloud DB ni simulate chesthunnam)
    cloud = sqlite3.connect('cloud.db')
    cloud.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, course TEXT)')
    cloud.execute('DELETE FROM students')
    for row in data:
        cloud.execute('INSERT INTO students VALUES (?, ?, ?)', row)
    cloud.commit(); cloud.close()
    return data

@app.route('/')
def dashboard():
    data = migrate()
    rows = "".join([f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td> Migrated</td></tr>" for r in data])
    return f"""
    <html><head><title>Cloud Database Migration - Sailaja</title>
    <style>
    body{{font-family:Arial;background:#0f172a;color:white;padding:15px;text-align:center}}
    h1{{color:#38bdf8}} .box{{background:#1e293b;padding:15px;border-radius:12px;margin:10px}}
    .success{{background:#14532d;padding:12px;border-radius:10px;font-weight:bold}}
    table{{width:100%;background:#1e293b;border-radius:10px;border-collapse:collapse;margin-top:10px}}
    th,td{{padding:10px;border-bottom:1px solid #334155}}
    </style></head><body>
    <h1>CLOUD DATABASE MIGRATION</h1>
    <p>Author: Injarapu Sailaja | ID: CITS9613 | Local SQLite - Cloud RDS (Simulated)</p>
    <div class="success">Migration Successful! {len(data)} Records Migrated from Local to Cloud!</div>
    <div class="box"><b>Source:</b> Local Database (local.db) --&gt; <b>Destination:</b> Cloud Database (cloud.db / AWS RDS)</div>
    <table><tr><th>ID</th><th>Name</th><th>Course</th><th>Status</th></tr>{rows}</table>
    <p>Migration Steps: 1. Backup Local DB 2. Create Cloud DB 3. Transfer Data 4. Verify Data</p>
    </body></html>
    """

@app.route('/api/migration-status')
def status():
    data = migrate()
    return jsonify({"source":"local.db","destination":"cloud.db (AWS RDS)","records_migrated":len(data),"status":"SUCCESS","migrated_by":"Injarapu Sailaja - CITS9613"})

if __name__ == '__main__':
    app.run(debug=True)