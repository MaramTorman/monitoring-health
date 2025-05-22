from influxdb_client import InfluxDBClient, Point, WriteOptions

bucket = "health_data"
org = "my-org"
token = "mytoken"
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=WriteOptions(batch_size=1))

patients = [
    ("Sarah", 180),    # abnormal
    ("Omar", 140),
    ("Lina", 85),
    ("Khalid", 170)    # abnormal
]                                                                                                                                                                                                                                                                  n                                                                                                                            
for name, hr in patients:
    point = Point("vitals").tag("patient", name).field("heart_rate", hr)
    write_api.write(bucket=bucket, org=org, record=point)

print("✅ تمت إضافة قياسات النبض")

client.close()
