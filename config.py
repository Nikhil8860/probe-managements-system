from flask import Flask

pms_app = Flask(__name__)

HOST = "127.0.0.1"
PORT = 5000
DEBUG = True

API = """http://92.97.130.6:8086/query?db=eProbeDB&q=SELECT time as DateTime,AppName,Region,SiteName,MobileTechnology,
        MobileNumber,MobileModel,DeviceID,MobileOSVersion,Jitter,PacketLoss,DownloadThroughput,UploadThroughput 
        FROM MobileAppsPerformance 
        WHERE time > now() - 2h AND AppName='Ookla' AND Region = {} AND SiteName = 'EXPO Main Office'"""
