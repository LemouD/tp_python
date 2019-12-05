import requests
import json

r = requests.get("http://swiv.outofpluto.com:5000/api/devices")
j = r.json()
j = {row["id"]: {"name": row["name"], "rssi": row["rssi"]} for row in j}
print(j)
print(r.text)

with open("devices.json", "w") as f:
  f.write(json.dumps(j))
