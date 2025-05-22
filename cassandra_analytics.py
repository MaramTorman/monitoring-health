from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

# إنشاء Keyspace إذا مش موجود
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS healthcare 
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
""")

# استخدام الـ keyspace
session.set_keyspace('healthcare')

# حذف الجدول إذا كان موجودًا
session.execute("DROP TABLE IF EXISTS analytics")

# إنشاء جدول جديد مع تقسيم حسب المنطقة
session.execute("""
    CREATE TABLE IF NOT EXISTS analytics (
        region text,
        patient text,
        metric text,
        value double,
        PRIMARY KEY ((region), patient, metric)
    )
""")

# بيانات التحليلات حسب المنطقة والمريض
data = [
    ("north", "Sarah", "average_heart_rate", 177.5),
    ("south", "Omar", "average_blood_pressure", 138.2),
    ("north", "Lina", "average_heart_rate", 82.0),
    ("north", "Khalid", "average_blood_pressure", 145.7)
]

# إدخال البيانات في الجدول
for entry in data:
    session.execute("""
        INSERT INTO analytics (region, patient, metric, value)
        VALUES (%s, %s, %s, %s)
    """, entry)

# استعراض البيانات للمنطقة "north"
rows = session.execute("SELECT * FROM analytics WHERE region='north'")
for row in rows:
    print(row)


