#SwitchScripts.py goals:
#Support Dell & Cisco IOS
#Support Telnet & Console(Serial DE-9 specifically)
#Designed to expedite initial setup of a switch when a backup config isn't available
#functions for bulk add vlans (either parsing a vlan db file || raw input)
#setup ip / subnet / gw / dns (raw input)
#banner / motd config
#super stretch goal of handling port tagging / trunking






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
tn = telnetLib.Telnet(host)




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
		tn.write("vlan " + vlanNum + "\n")
		tn.write("name " + vlanName + "\n")
		tn.write("exit\n")

		
		
		
	
	
	