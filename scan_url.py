import requests
import json
from orm import sessionmaker, Device
from sqlalchemy import create_engine
from datetime import datetime


engine = create_engine('sqlite:///epydeble.db')
session = sessionmaker()
session.configure(bind=engine)
s = session()

def scan_url():
  r = requests.get("http://swiv.outofpluto.com:5000/api/devices")
  j = r.json()
  j = {row["id"]: {"name": row["name"], "rssi": row["rssi"]} for row in j}
  print(j)
  print(r.text)
  with open("devices.json", "w") as f:
    f.write(json.dumps(j))

  date = datetime.now()
  print(date)
  for row in r.json():
   device = Device(mac_address=row["id"], name=row["name"], rssi=row["rssi"], date_scan=date)
   print(device.getinfo())
   s.add(device)

  s.commit()
  print("All devices : ")
  for p in s.query(Device).all():
    print(p)

  print('test')

scan_url()
