#!/usr/bin/env python3

''' Dell PowerConnect 3xxx5xxx series auto backup script parses file
'dellSwitches' for IPs to telnet and copy backup configuration '''

import telnetlib
import time
import datetime
from config import CONFIG


# setup username and password creds for telnet session
user = CONFIG.get('DELL', 'USERNAME')
password = CONFIG.get('DELL', 'PASSWORD')
now = datetime.datetime.now()
timestamp = (str(now.month) + "-" + str(now.day) + "-" + str(now.year))


def dell_login():
    ''' pass login credentials to telnet session '''
    tn.read_until("User Name:")
    tn.write(user + "\n")
    tn.read_until("Password:")
    tn.write(str(password) + "\n")


def dell_get_backup():
    ''' set datadump mode to remove need for user input on bulk data dump dump
    runningcfg and save to file '''
    tn.read_until("#")
    tn.write("terminal datadump\n")
    tn.read_until("#")
    tn.write("show running-config\n")
    # sleep after show running config for command to finish
    time.sleep(10)
    config_output = tn.read_very_eager()
    backup_config = open(str(host) + "-" + timestamp, "w")
    backup_config.write(config_output)
    backup_config.close()
    tn.write("exit\n")

# file path to dellSwitches
f = open("dellSwitches")
# main loop - run two functions on each IP found in dellSwitches file
for line in f:
    print("Connecting to switch {}", str(line))
    host = line.strip()

    tn = telnetlib.Telnet(host)

    dell_login()
    dell_get_backup()

f.close()
