from sqlalchemy import Column, Boolean, String, Integer, Numeric, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()


class Device(Base):
  __tablename__ = 'devices'
  id = Column(Integer, primary_key=True)
  mac_address = Column('mac_address', String)
  name = Column('name', String(32))
  rssi = Column('rssi', Integer)
  date_scan = Column('date', DateTime)

  def __str__(self):
    return "nom: " + self.name+ " date: " + self.date_scan.strftime("%Y/%m/%d %H:%M:%S")
  def getinfo(self):
    return "nom: " + self.name + " date: " + self.date_scan.strftime("%Y/%m/%d %H:%M:%S")

engine = create_engine('sqlite:///:memory:')

from sqlalchemy.orm import sessionmaker

session = sessionmaker()
session.configure(bind=engine)
s = session()

Base.metadata.create_all(engine)

date = datetime.now()
#product = Device(mac_address="B8:81:98:4A:A2:4E", name="Nevaeh", rssi= -62, date=date)
#s.add(product)
#product = Device(mac_address="7C:A1:77:C4:6C:59", name="H_Zak", rssi= -59, date=date)
#s.add(product)
#print("---- print 1 ----")
#for p in s.query(Device).all():
#  print(p)
#s.commit()
#s.delete(product)
#s.commit()
#print("---- print 2 ----")
#for p in s.query(Device).all():
#  print(p)