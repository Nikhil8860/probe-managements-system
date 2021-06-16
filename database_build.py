import os
from db_config import db
from models.fault_management import fault_model
from models.performance_analysis import performance_model
from models.device_management import device_model
from datetime import datetime, timedelta


start_date = datetime.now() - timedelta(days=7)
start_date = datetime.strptime(start_date.strftime('%d/%m/%Y'), '%d/%m/%Y').date()
end_date = datetime.strptime(datetime.now().strftime('%d/%m/%Y'), '%d/%m/%Y').date()

# Data to initialize database with
PMS = [
    {"start_date": start_date, "end_date": end_date, "region": "Dubai", "site_name": "EXPO Main Office",
     "probe": "DROPBOX", "app_type": "Dropbox"},
    {"start_date": start_date, "end_date": end_date, "region": "Dubai", "site_name": "Mall of emirates",
     "probe": "FACEBOOK", "app_type": "Facebook"},
    {"start_date": start_date, "end_date": end_date, "region": "Dubai", "site_name": "Taj mahal", "probe": "INSTAGRAM",
     "app_type": "Whatsapp"},
    {"start_date": start_date, "end_date": end_date, "region": "Dubai", "site_name": "Lal Quila", "probe": "TWILLIO",
     "app_type": "Twitter"},
    {"start_date": start_date, "end_date": end_date, "region": "Dubai", "site_name": "Jama Masjid", "probe": "SNAPCHAT",
     "app_type": "Instagram"},
    {"start_date": start_date, "end_date": end_date, "region": "Dubai", "site_name": "Shahdara", "probe": "LINKDIN",
     "app_type": "Skype"},
    {"start_date": start_date, "end_date": end_date, "region": "Dubai", "site_name": "Burj Khalifa", "probe": "LINKDIN",
     "app_type": "Dropbox"},
    {"start_date": start_date, "end_date": end_date, "region": "Dubai", "site_name": "Tower of Hanoi",
     "probe": "FACEBOOK", "app_type": "Facebook"},
    {"start_date": start_date, "end_date": end_date, "region": "Dubai", "site_name": "EXPO Main Office",
     "probe": "INSTAGRAM", "app_type": "Instagram"},
    {"start_date": start_date, "end_date": end_date, "region": "Dubai", "site_name": "EXPO Main Office",
     "probe": "DROPBOX", "app_type": "Whatsapp"},
]
# planet = DeviceManagement.query.filter_by(probe='AAAAA').first()
# db.session.delete(planet)
# db.session.commit()
# print("Deleted")
# quit()
# Delete database file if it exists currently
# if os.path.exists("probe_management_system.db"):
#     os.remove("probe_management_system.db")

# Create the database
db.create_all()
# iterate over the PEOPLE structure and populate the database
for site in PMS:
    p = performance_model.PerformanceAnalysis(start_date=site.get("start_date"), end_date=site.get("end_date"), region=site.get('region'),
                                              site_name=site.get('site_name'), probe=site.get('probe'),
                                              app_type=site.get('app_type'))
    db.session.add(p)

db.session.commit()


dm_data = PMS = [

    {'probe_name': "AUH", 'region': "Dubai", 'site_name': "xxx Pavalion", 'mobile_technology': "Andriod",
     "mobile_model": "samsung guru", "cordinates": "1,2", "date_of_installation": end_date, 'device_id': "De7sadjsf82",
     'mobile_number': 935763457345, 'mobile_os': "935763457345", 'current_version': "2.0", 'update': "update to 2.1",
     'remote_management': "Remote Access"},
    {'probe_name': "AUH", 'region': "Dubai", 'site_name': "xxx Pavalion", 'mobile_technology': "Andriod",
     "mobile_model": "samsung guru", "cordinates": "1,2", "date_of_installation": end_date, 'device_id': "De7sadjsf82",
     'mobile_number': 935763457345, 'mobile_os': "935763457345", 'current_version': "2.0", 'update': "update to 2.1",
     'remote_management': "Remote Access"},
    {'probe_name': "AUH", 'region': "Dubai", 'site_name': "xxx Pavalion", 'device_id': "De7sadjsf82",
     'mobile_number': 935763457345, 'mobile_os': "935763457345", 'current_version': "2.0", 'update': "update to 2.1",
     'remote_management': "Remote Access"},
    {'probe_name': "AUH", 'region': "Dubai", 'site_name': "xxx Pavalion", 'mobile_technology': "Andriod",
     "mobile_model": "samsung guru", "cordinates": "1,2", "date_of_installation": end_date, 'device_id': "De7sadjsf82",
     'mobile_number': 935763457345, 'mobile_os': "935763457345", 'current_version': "2.0", 'update': "update to 2.1",
     'remote_management': "Remote Access"},
    {'probe_name': "AUH", 'region': "Dubai", 'site_name': "xxx Pavalion", 'mobile_technology': "Andriod",
     "mobile_model": "samsung guru", "cordinates": "1,2", "date_of_installation": end_date, 'device_id': "De7sadjsf82",
     'mobile_number': 935763457345, 'mobile_os': "935763457345", 'current_version': "2.0", 'update': "update to 2.1",
     'remote_management': "Remote Access"},
    {'probe_name': "AUH", 'region': "Dubai", 'site_name': "xxx Pavalion", 'mobile_technology': "Andriod",
     "mobile_model": "samsung guru", "cordinates": "1,2", "date_of_installation": end_date, 'device_id': "De7sadjsf82",
     'mobile_number': 935763457345, 'mobile_os': "935763457345", 'current_version': "2.0", 'update': "update to 2.1",
     'remote_management': "Remote Access"},
    {'probe_name': "AUH", 'region': "Dubai", 'site_name': "xxx Pavalion", 'mobile_technology': "Andriod",
     "mobile_model": "samsung guru", "cordinates": "1,2", "date_of_installation": end_date, 'device_id': "De7sadjsf82",
     'mobile_number': 935763457345, 'mobile_os': "935763457345", 'current_version': "2.0", 'update': "update to 2.1",
     'remote_management': "Remote Access"},
    {'probe_name': "AUH", 'region': "Dubai", 'site_name': "xxx Pavalion", 'mobile_technology': "Andriod",
     "mobile_model": "samsung guru", "cordinates": "1,2", "date_of_installation": end_date, 'device_id': "De7sadjsf82",
     'mobile_number': 935763457345, 'mobile_os': "935763457345", 'current_version': "2.0", 'update': "update to 2.1",
     'remote_management': "Remote Access"},
    {'probe_name': "AUH", 'region': "Dubai", 'site_name': "xxx Pavalion", 'mobile_technology': "Andriod",
     "mobile_model": "samsung guru", "cordinates": "1,2", "date_of_installation": end_date, 'device_id': "De7sadjsf82",
     'mobile_number': 935763457345, 'mobile_os': "935763457345", 'current_version': "2.0", 'update': "update to 2.1",
     'remote_management': "Remote Access"},
    {'probe_name': "AUH", 'region': "Dubai", 'site_name': "xxx Pavalion", 'mobile_technology': "Andriod",
     "mobile_model": "samsung guru", "cordinates": "1,2", "date_of_installation": end_date, 'device_id': "De7sadjsf82",
     'mobile_number': 935763457345, 'mobile_os': "935763457345", 'current_version': "2.0", 'update': "update to 2.1",
     'remote_management': "Remote Access"},
]

for site in dm_data:
    p = device_model.DeviceManagement(probe_name=site.get("probe_name"), region=site.get("region"),
                                      site_name=site.get('site_name'),
                                      mobile_technology=site.get('mobile_technology'),
                                      mobile_model=site.get('mobile_model'),
                                      cordinates=site.get('cordinates'),
                                      date_of_installation=site.get('date_of_installation'),
                                      device_id=site.get('device_id'),
                                      mobile_number=site.get('mobile_number'),
                                      mobile_os=site.get('mobile_os'),
                                      current_version=site.get('current_version'),
                                      update=site.get('update'),
                                      remote_management=site.get('remote_management'),
                                      )
    db.session.add(p)

db.session.commit()


fault_data = [
    {'time': start_date, 'probe_id': 1234, 'region': "Dubai", 'site_name': "XXX pavallion",
     "ip": "192.168.1.17", "fault_description": "power supply faliur", 'current_version': "2.0", 'status': "active",
     'ack_by': "Nikhil", "ack_time": end_date},
    {'time': start_date, 'probe_id': 1234, 'region': "Dubai", 'site_name': "XXX pavallion",
     "ip": "192.168.1.17", "fault_description": "power supply faliur", 'current_version': "2.0", 'status': "active",
     'ack_by': "Nikhil", "ack_time": end_date},
    {'time': start_date, 'probe_id': 1234, 'region': "Dubai", 'site_name': "XXX pavallion",
     "ip": "192.168.1.17", "fault_description": "power supply faliur", 'current_version': "2.0", 'status': "active",
     'ack_by': "Nikhil", "ack_time": end_date},
    {'time': start_date, 'probe_id': 1234, 'region': "Dubai", 'site_name': "XXX pavallion",
     "ip": "192.168.1.17", "fault_description": "power supply faliur", 'current_version': "2.0", 'status': "active",
     'ack_by': "Nikhil", "ack_time": end_date},
    {'time': start_date, 'probe_id': 1234, 'region': "Dubai", 'site_name': "XXX pavallion",
     "ip": "192.168.1.17", "fault_description": "power supply faliur", 'current_version': "2.0", 'status': "active",
     'ack_by': "Nikhil", "ack_time": end_date}
]

for site in fault_data:
    p = fault_model.FaultManagement(time=site.get("time"), probe_id=site.get("probe_id"), region=site.get('region'),
                                     site_name=site.get('site_name'), ip=site.get('ip'),
                                     fault_description=site.get('fault_description'),
                                     current_version=site.get('current_version'), status=site.get('status'),
                                     ack_by=site.get('ack_by'), ack_time=site.get('ack_time'))
    db.session.add(p)

    db.session.commit()
