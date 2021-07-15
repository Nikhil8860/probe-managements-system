from influxdb import InfluxDBClient

db = InfluxDBClient('localhost', 8086, 'root', 'root', 'eProbeDB')
print(db.query('SHOW databases'))
