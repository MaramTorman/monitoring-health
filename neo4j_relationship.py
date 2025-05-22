from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "testpass"))  # غيّري الباسورد إذا غيرتيها

def create_entities(tx):
    # بيانات الربط بين الطبيب والمريض
    relations = [
        ("Sarah", "Dr. Lina"),
        ("Omar", "Dr. Sami"),
        ("Lina", "Dr. Huda"),
        ("Khalid", "Dr. Ahmed")
    ]

    for patient, doctor in relations:
        tx.run("MERGE (:Patient {name: $patient})", patient=patient)
        tx.run("MERGE (:Doctor {name: $doctor})", doctor=doctor)
        tx.run("""
            MATCH (p:Patient {name: $patient}), (d:Doctor {name: $doctor})
            MERGE (d)-[:TREATS]->(p)
        """, patient=patient, doctor=doctor)

with driver.session() as session:
    session.write_transaction(create_entities)

print("✅ تم ربط كل الأطباء بالمرضى")
