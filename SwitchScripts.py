#SwitchScripts.py goals:
#Support Dell & Cisco IOS
#Support Telnet & Console(Serial DE-9 specifically)
#Designed to expedite initial setup of a switch when a backup config isn't available
#functions for bulk add vlans (either parsing a vlan db file || raw input)
# # ability to add a vlan(s) to a group of switches
#setup ip / subnet / gw / dns (raw input)
#banner / motd config
#super stretch goal of handling port tagging / trunking
#Look into NetMiko for ssh python library // this may end up being two diff scripts



#!/usr/bin/env python

#import libraries
import getpass
import sys
import telnetlib

#declare and init vars
host = raw_input("Enter host ip: ")
user = raw_input("Enter telnet username: ")
password = getpass.getpass()
privpassword = getpass.getpass()

#create telnet session to host
tn = telnetlib.Telnet(host)




#cisco telnet login
def ciscoTelnetLogin(host, user, password):
    #parse screen until username requested & #send username
    tn.read_until("Username: ")
    tn.write(user + "\n")
    #check for pw and send if detected
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    #enable priv mode and send pw
    tn.write("enable\n")
    tn.write(privpassword)

#cisco terminate telnet session	+ save changes
def ciscoTelnetClose():
    tn.write("end\n")
    tn.write("wr\n")
    tn.write("exit\n")


#cisco vlan automation
def ciscoBulkVlan():
    #declare number of vlans to be added // maybe refactor
    numVlans = raw_input("How many VLANs do you want to define?: ")
    #enter configure terminal mode
    tn.write("conf t \n")
    #get vlan number and name then add vlan to switch vlan db
    for x in range(1, numVlans):
        vlanNum = raw_input("Enter VLAN #: ")
        vlanName = raw_input("Enter VLAN name: ")
        tn.write("vlan " + str(vlanNum) + "\n")
        tn.write("name " + str(vlanName) + "\n")
        tn.write("exit\n")



#for debug purposes display console i/o
print(tn.read_all())

#Dell PowerConnect telnet login
def dellTelnetLogin(host, user, password):
    tn.read_until("User Name: ")
    tn.write(user + "\n")
    #no need for enable mode on dell - make sure to enter config mode for other funcs
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")


#cisco auto backup
def ciscoBackup():
	#after logging into switch (make sure not in conf t mode)
	#

	#set terminal length to 0 so full config can be dumped without user input (changing pages)
	tn.write("terminal length 0\n")
	#show running-config
	tn.write("show run\n")
	#close session
	tn.write("exit\n")
	#store output in var named configOutput
	configOutput = tn.read_all()
	#open a file called switch and IP and set it to writeable
	#might be useful to incorporate date + time in file name -- come back to this
	backupConfig = open("switch" + host, "w")
	#copy configOutput contents to the file and then close file.
	backupConfig.write(configOutput)
	backupConfig.close



#parsing file for switches - switch db file myswitches
#will tie this into other functions, just keeping for theory
#maybe create program db of switches and names for interacting? dictionary etc
def checkSwitchDB():
	#open local file named myswitches
	f = open('myswitches')

	#parse file and grab each line
	for line in f:
		print("Connecting to switch " + (line))
		host = line.strip()

	f.close()
