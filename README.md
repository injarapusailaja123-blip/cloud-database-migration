
# Codtech Intern Task 4 - Cloud Database Migration

**Name:** Injarapu Sailaja
**Intern ID:** CITS9613
**Domain:** Cloud Computing
**Task:** Task 4

## Objective
Local Database lo unna data ni Cloud Database (AWS RDS) lo ki Migration cheyadam. Data loss avvakunda, correct ga transfer cheyadam.

## Tools Used
Python, Flask, SQLite (Local DB), AWS RDS Concept, HTML, CSS

## Migration Process
1.  **Backup:** Local Database (local.db) nunchi data teesukovadam
2.  **Create Cloud DB:** Cloud lo kotta Database (cloud.db / RDS) create cheyadam
3.  **Transfer:** Local data ni Cloud DB lo ki copy cheyadam
4.  **Verify:** Cloud lo data correct ga vachinda check cheyadam - 3 Records Verified

## Features
- Source: Local Database (local.db)
- Destination: Cloud Database (cloud.db - AWS RDS Simulated)
- API: /api/migration-status - Migration status chupisthundi
- Data Verification: Migration tarvata data count compare chesthundi

## How to Run
pip install flask
python app.py
Browser lo open cheyandi: http://127.0.0.1:5000

## Results
- Local DB Records: 3
- Cloud DB Records After Migration: 3
- Status: SUCCESS - No Data Loss!
- Records: (1, Sailaja, Cloud Computing), (2, Priya, Python), (3, Ram, AWS) - All Migrated!

## Conclusion
Ee project valla Database Migration ela chestharo nerchukunnanu. Real life lo companies Local Server nunchi AWS RDS ki ilage migrate chestharu. Backup teesukuni, verify chesi migrate chesthe data loss undadu.