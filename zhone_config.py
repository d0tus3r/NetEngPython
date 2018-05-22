#!/usr/bin/env python3
'''Run script with two params:
@password = last 6 of serial #
@filename = config_file.conf'''

import telnetlib
import time
import sys
from config import CONFIG

#Will move static vars to config file
USERNAME = "admin"
PASSWORD = "admin" + sys.argv[1]
HOST = "192.168.1.1"
FILENAME = sys.argv[2]
TFTP_HOST = "192.168.1.169"


def zhone_login():
    ''' pass login credentials to telnet session '''
    TN.read_until(b"Login:")
    TN.write(USERNAME.encode('ascii') + b"\n")
    TN.read_until(b"Password:")
    TN.write(str(PASSWORD).encode('ascii') + b"\n")

def zhone_config():
    '''After telnet session established and authentication successful:
    run tftp command with config file specified as parameter on script exec'''
    TN.read_until(b">")
    #tftp command - might have tftp_host be a config param
    TN.write(b"tftp -g -t c -f " + FILENAME.encode('ascii') + b" " +\
        TFTP_HOST.encode('ascii'))
    time.sleep(20)

'''Stretch Goals:
Loop through folder of config files with a progress indicator of when to unplug
previous modem && when to init login to new modem.
Look through docs to see if doable through ping response parsing.'''




#main loop
TN = telnetlib.Telnet(HOST)
zhone_login()
zhone_config()
