#!/usr/bin/env python3

''' Planet DSLAM bridging bug fix '''

import telnetlib
import time
from config import CONFIG

# setup username and password creds for telnet session
USER = CONFIG.get('PLANET', 'USERNAME')
PASSWORD = CONFIG.get('PLANET', 'PASSWORD')
HOST = input('Enter PLANET Dslam IP: ')
PORT = input('Enter the port: ')
BRIDGE_NUMBER = input('Enter bridge port to reset: ')
PVC = input('Enter PVC port: ')
VLAN = input('Enter native vlan: ')
SERV_PROFILE = input('Enter service profile number: ')


def planet_login():
    ''' pass login credentials to telnet session '''
    TN.read_until(b'IDL-2402 login:')
    TN.write(USER.encode('ascii') + b'\n')
    TN.read_until(b'Password:')
    TN.write(str(PASSWORD).encode('ascii') + b'\n')
    TN.read_until(b'IDL-2402:>')
    TN.write(b'enable\n')
    TN.read_until(b'IDL-2402:%')
    TN.write(b'configure\n')

def planet_bridge_reset():
    ''' commands related to bridge reset - needs port, vlan, pvc #'''
    TN.read_until(b'IDL-2402:(conf)#')
    str_in = 'interface xdsl {}'.format(PORT)
    TN.write(str_in.encode('ascii') + b'\n')
    time.sleep(2)
    TN.read_until(b'IDL-2402:(intf-conf)#')
    str_in = 'bridge {} disable'.format(BRIDGE_NUMBER)
    TN.write(str_in.encode('ascii') + b'\n')
    time.sleep(2)
    TN.read_until(b'IDL-2402:(intf-conf)#')
    str_in = 'bridge {} pvc 0/{}'.format(BRIDGE_NUMBER, PVC)
    TN.write(str_in.encode('ascii') + b'\n')
    time.sleep(2)
    TN.read_until(b'IDL-2402:(bridge-atm-conf)#')
    TN.write(b'pvc encapsulation auto')
    time.sleep(2)
    TN.read_until(b'IDL-2402:(bridge-atm-conf)#')
    str_in = 'default vlan {}'.format(VLAN)
    TN.write(str_in.encode('ascii') + b'\n')
    time.sleep(2)
    TN.read_until(b'IDL-2402:(bridge-atm-conf)#')
    TN.write(b'exit')
    time.sleep(2)
    TN.read_until(b'IDL-2402:(intf-conf)#')
    TN.write(b'adsl-config')
    time.sleep(2)
    TN.read_until(b'IDL-2402:(adsl-intf-conf)#')
    str_in = 'line profile service {}'.format(SERV_PROFILE)
    TN.write(str_in.encode('ascii') + b'\n')
    time.sleep(2)
    TN.read_until(b'IDL-2402:(adsl-intf-conf)#')
    TN.write(b'line status service reset')
    time.sleep(2)
    TN.read_until(b'IDL-2402:(adsl-intf-conf)#')
    TN.write(b'exit')
    time.sleep(2)
    TN.read_until(b'IDL-2402:(intf-conf)#')
    TN.write(b'exit')
    time.sleep(2)
    TN.read_until(b'IDL-2402:(conf)#')
    TN.write(b'exit')
    time.sleep(2)
    TN.read_until(b'IDL-2402:%')
    TN.write(b'exit')
    time.sleep(2)
    TN.read_until(b'IDL-2402:>')
    TN.write(b'exit')
    time.sleep(2)




TN = telnetlib.Telnet(HOST)
planet_login()
planet_bridge_reset()
time.sleep(10)
