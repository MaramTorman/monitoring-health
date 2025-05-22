from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["healthCare"]
patients = db["patients"]

sample_patients = 
    {"name": "Sarah", "age": 33, "history": ["asthma"], "region": "north"},
    {"name": "Omar", "age": 45, "history": ["hypertension"], "region": "south"},
    {"name": "Lina", "age": 29, "history": ["diabetes"], "region": "north"},
    {"name": "Khalid", "age": 60, "history": ["heart disease"], "region": "north"}
    {"name": "x", "age": 50, "history": ["diabetes"], "region": "north"}
patients.insert_many(sample_patients)

for p in patients.find({"region": "north"}):
    print(p)
