#Dell PowerConnect 3xxx5xxx series auto backup script
#parses file 'dellSwitches' for IPs to telnet and copy backup configuration

#import necessary libraries
import getpass
import sys
import telnetlib
import time
import datetime


#setup username and password creds for telnet session
user = raw_input("Enter username for telnet session: ")
password = getpass.getpass()
now = datetime.datetime.now()
timestamp = (str(now.month) + "-" + str(now.day) + "-" + str(now.year))

#pass login credentials to telnet session
def dellLogin():
    tn.read_until("User Name:")
    tn.write(user + "\n")
    tn.read_until("Password:")
    tn.write(str(password) + "\n")

#set datadump mode to remove need for user input on bulk data dump
#dump runningcfg and save to file
def dellGetBackup():
    tn.read_until("#")
    tn.write("terminal datadump\n")
    tn.read_until("#")
    tn.write("show running-config\n")
    #sleep after show running config for command to finish
    time.sleep(10)
    configOutput = tn.read_very_eager()
    backupConfig = open(str(host) + "-" + timestamp, "w")
    backupConfig.write(configOutput)
    backupConfig.close()
    tn.write("exit\n")

#file path to dellSwitches
f = open("dellSwitches")
#main loop - run two functions on each IP found in dellSwitches file
for line in f:
    print "Connecting to switch " + str(line)
    host = line.strip()
    
    tn = telnetlib.Telnet(host)
     
    dellLogin()
    dellGetBackup()

f.close()

