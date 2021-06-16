from pysnmp.hlapi import *
import os

"""
Total RAM in machine: .1.3.6.1.4.1.2021.4.5.0
Total RAM used: .1.3.6.1.4.1.2021.4.6.0

(total_ram_used/total_ram_in_machine) * 100  -- memory percentage

percentages of system CPU time: .1.3.6.1.4.1.2021.11.10.0

fault description will be print when percentage is more that 80% from CPU and memory then generate alert

for interface
-------------------
cat /sys/class/net/eno1/operstate   if this is down then generate alarms 

Interface utilization this will come from OIDs only
interface status
"""


def get_data_from_oids(oids):
    """
    oids dictonary of all the oids cpu, memory
    """
    fault = {}
    interface_status = os.popen('cat /sys/class/net/eno1/operstate')
    for key, val in oids.items():
        if len(val) == 1:
            g = getCmd(
                SnmpEngine(), CommunityData('Ex@mPL3'), UdpTransportTarget(
                    ('10.0.2.15', 161)), ContextData(), ObjectType(
                    ObjectIdentity(val[0]))
            )
            error_indication, error_status, error_index, var_binds = next(g)
            for var_bind in var_binds:
                res = '='.join([x.prettyPrint() for x in var_bind]).split('=')[1]
                fault[key] = res

        if len(val) > 1:
            for i in val:
                g = getCmd(
                    SnmpEngine(), CommunityData('Ex@mPL3'), UdpTransportTarget(
                        ('10.0.2.15', 161)), ContextData(), ObjectType(
                        ObjectIdentity(i))
                )
                error_indication, error_status, error_index, var_binds = next(g)
                for var_bind in var_binds:
                    res = '='.join([x.prettyPrint() for x in var_bind]).split('=')[1]
                    fault.setdefault(key, []).append(res)

    a, b = fault.get('memory')
    fault['memory'] = (int(a) / int(b)) * 100
    fault['interface'] = interface_status.read().replace('\n', '')
    print(fault)
    fault['cpu'] = 'cpu alert' if float(fault.get('cpu')) > 80.0 else "No alert for cpu"
    fault['memory'] = 'memory alert' if float(fault.get('memory')) > 80.0 else "No alert for memory"
    fault['interface'] = 'interface alert' if fault.get('interface').lower() == 'dowm' else "No alert for interface"
    return fault


if __name__ == '__main__':
    oids_dict = {
        "cpu": [".1.3.6.1.4.1.2021.11.10.0"],
        "memory": ['.1.3.6.1.4.1.2021.4.6.0', '.1.3.6.1.4.1.2021.4.11.0']
    }
    get_data_from_oids(oids_dict)
