#!/usr/bin/env python3

''' Planet DSLAM bridging bug fix '''

import telnetlib
import time
from config import CONFIG

# setup username and password creds for telnet session
USER = CONFIG.get('PLANET', 'USERNAME')
PASSWORD = CONFIG.get('PLANET', 'PASSWORD')
HOST = input('Enter PLANET Dslam IP: ')


def planet_login():
    ''' pass login credentials to telnet session '''
    TN.read_until(b'IDL-2402 login:')
    TN.write(USER.encode('ascii') + b'\n')
    TN.read_until(b'Password:')
    TN.write(str(PASSWORD).encode('ascii') + b'\n')
    TN.read_until(b'IDL-2402:>')
    TN.write(b'enable\n')
    TN.read_until(b'IDL-2402:#')
    TN.write(b'configure\n')

def planet_bridge_reset():
    ''' commands related to bridge reset - needs port, vlan, pvc #'''
    TN.read_until('')





TN = telnetlib.Telnet(HOST)
planet_login()
