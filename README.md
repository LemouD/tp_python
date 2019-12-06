# epydeble

epydeble is a project which goal is to display nearby bluetooth devices on a web page.

## requirements

   - python > 3.6
   - modules in requirements.txt
   - ``pip install requests``
   - ``pip install SQLAlchemy``
   - http://swiv.outofpluto.com/api/devices accessible
   - in a python console: 
     + ``from orm import Device, Base``
     + ``from sqlalchemy import create_engine``
     + ``engine = create_engine("sqlite:///epydeble.db")``
     + ``Base.metadata.create_all(engine)``

## how to   

The code currently provides two simple scripts:

	- `scan_url.py`: scan devices and store them in a json and in  file with their ids, mac  address, names, date and RSSI.
	- `app.py`: simple Flask app : 
        - http://127.0.0.1:5000/all_devices : to see all scaned devices
        - http://127.0.0.1:5000/: to see last scaned devices and a not functional button 'scan' 
           to execute 'scan_url.py' and refresh homepage
        

An devices.json file is provided as an example.
The bluetooth code in `blscan` uses PyBluez library.

