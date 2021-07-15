import os
from db_config import db
import pandas as pd
from models.performance_analysis import performance_model
from models.domain import domain_model
from models.networks import network_model
from models.probe_monitoring import probe_model
from models.webservices import web_service_model
from models.fault_management import fault_model
import xlrd
from datetime import datetime

xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

db.create_all()

# fault_data = [
#     {'url_name': 'www.google.com'},
#     {'url_name': 'www.youtube.com'},
#     {'url_name': 'www.twitter.com'},
#     {'url_name': 'www.instagram.com'},
#     {'url_name': 'www.facebook.com'},
#     {'url_name': 'www.whatsapp.com'},
# ]
#
# for site in fault_data:
#     p = web_service_model.WebService(url_name=site.get("url_name"))
#     db.session.add(p)
# db.session.commit()

# fault_data = [
#     {'application_name': 'Dropbox'},
#     {'application_name': 'Facebook'},
#     {'application_name': 'Whatsapp'},
#     {'application_name': 'Snapchat'},
#     {'application_name': 'Twitter'},
#     {'application_name': 'Instagram'},
#     {'application_name': 'Skype'},
#     {'application_name': 'Ookla'},
#     {'application_name': 'SMS'},
#     {'application_name': 'Youtube'},
#     {'application_name': 'Dialer pad'},
#     {'application_name': 'My Etisalat'},
#
# ]
#
# for site in fault_data:
#     p = performance_model.Applications(application_name=site.get("application_name"))
#     db.session.add(p)
# db.session.commit()

domain_data = [
    {'domain_name': 'eProbe-UX'},
    {'domain_name': 'eProbe-NW'},
    {'domain_name': 'eProbe-5G'},
    {'domain_name': 'CreaNORD'},
    {'domain_name': 'EXFO'},
]
for site in domain_data:
    p = domain_model.Domain(domain_name=site.get("domain_name"))
    db.session.add(p)
db.session.commit()

# Give the location of the file
# loc = (r'D:\etislat\DB structure\pms-db_1.1.xlsx')
#
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_name('t_probe')
# for i in range(1, sheet.nrows):
#     probe_id = db.Column(db.Integer, db.Sequence('seq_probe_id', start=1, increment=1), primary_key=True)
#     device_id = sheet.cell_value(i, 1)
#     probe_display_name = sheet.cell_value(i, 2)
#     region = sheet.cell_value(i, 3)
#     site_name = sheet.cell_value(i, 4)
#     mobile_technology = sheet.cell_value(i, 5)
#     mobile_model = sheet.cell_value(i, 6)
#     mobile_number = sheet.cell_value(i, 7)
#     mobile_os = sheet.cell_value(i, 8)
#     mobile_os_version = sheet.cell_value(i, 9)
#     current_version = sheet.cell_value(i, 10)
#     current_status = sheet.cell_value(i, 11)
#     cordinates = sheet.cell_value(i, 12)
#     default_select = sheet.cell_value(i, 13)
#     installation_date = sheet.cell_value(i, 14)
#     #  10-06-2021  12:27:23
#     installation_date = datetime.strptime(installation_date, '%d-%m-%Y %H:%M:%S')
#     installation_by = sheet.cell_value(i, 15)
#     # print(installation_date)
#     p = probe_model.ProbeMonitoring(device_id=device_id, probe_display_name=probe_display_name, region=region,
#                                     site_name=site_name, mobile_technology=mobile_technology, mobile_model=mobile_model,
#                                     mobile_number=mobile_number, mobile_os=mobile_os,
#                                     mobile_os_version=mobile_os_version, current_version=current_version,
#                                     current_status=current_status, cordinates=cordinates, default_select=default_select,
#                                     installation_date=installation_date, installation_by=installation_by)
#
#     db.session.add(p)
# db.session.commit()

#
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_name('t_network')
# for i in range(1, sheet.nrows):
#     network_id = sheet.cell_value(i, 0)
#     network_name = sheet.cell_value(i, 1)
#     dpi = sheet.cell_value(i, 2)
#     probe_display_name = sheet.cell_value(i, 3)
#
#     # print(installation_date)
#     p = network_model.Network(network_id=network_id, network_name=network_name, dpi=dpi,
#                               network_display_name=probe_display_name)
#
#     db.session.add(p)
# db.session.commit()
