import redis
r = redis.Redis(host='localhost', port=6379)
#redis.Redis(host="192.168.1.20", port=6379)
alerts = {
    "Sarah": "⚠️ Heart rate 180 bpm",
    "Khalid": "⚠️ Heart rate 170 bpm"
}
for patient, alert in alerts.items():
    r.set(f"alert:patient:{patient}", alert, ex=300)  # ex = expires in 300 seconds
for patient in alerts:
    alert = r.get(f"alert:patient:{patient}")
    if alert:
        print(f"🔔 تنبيه لـ {patient}: {alert.decode()}")
    else:
        print(f"✅ لا يوجد تنبيه حالي لـ {patient}")

