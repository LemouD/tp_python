from flask import Flask, request, render_template, redirect, url_for
import json
from orm import sessionmaker, Device
from sqlalchemy import create_engine
from scan_url import scan_url


app = Flask(__name__)
app.debug

engine = create_engine('sqlite:///epydeble.db')
session = sessionmaker()
session.configure(bind=engine)

@app.route('/')
@app.route('/home.html')
def home():
  s = session()
  last_device = s.query(Device).order_by(Device.date_scan.desc()).first()
  last_devices = s.query(Device).filter(Device.date_scan == last_device.date_scan)
  return render_template("home.html", devices = last_devices)

@app.route('/devices', methods=['GET'])
def devices():
  devices = parse_from_json()
  return render_template("devices.html", devices=devices)

@app.route('/all_devices', methods=['GET'])
def all_devices():
  s = session()
  devices =  s.query(Device).all()
  return render_template("devices.html", devices=devices)

@app.route('/scan_url')
def scan_url():
  scan_url()
  return redirect(url_for('home'))


def parse_from_json():
  devices = []
  with open('./devices.json', 'r') as f:
    data = json.loads(f.read())
    for id in data:
      devices.append({"id": id,
                      "name": data[id]["name"],
                      "rssi": data[id]["rssi"] if "rssi" in data[id] else "?"})
    return devices

def dump_to_json(devices):
  pass

if __name__ == "__main__":
  app.run("127.0.0.1")