import socket
import subprocess
import sys
import os, platform
#function to find the nth occurence of a character in a string
def findNthOccurence(x, y, n):
    start = x.find(y)
    while start >= 0 and n > 1:
        start = x.find(y, start+len(y))
        n -= 1
    return start
#scan IP
def ping(h):
    #returns if host responds to ping
    pingStr = "-n 1" if  platform.system().lower(
            )=="windows" else "-c 1"
    return os.system("ping " + pingStr + " " + h) == 0

addressInput=input("Input IP (Example: 172.16.8.214/26)\n") #get input from user

#get info on subnet
ipAddress=addressInput.split('/')
index=findNthOccurence(ipAddress[0],'.',3)
ipString=ipAddress[0][:-1]

#check computers on the network
for i in range(0,int(ipAddress[1])):
        if(ping(ipString+str(i))==True):
                print(ipString+str(i))

#scan ports
userinput="Y"
count=0
while(userinput.upper()=="Y"):
        #get input host from user
        remoteserver = input("Input host to scan ports: ")
        remoteServerIP = remoteserver

        print ("Scanning", remoteServerIP)

        # scan ports in range from 1 to 1024
        try:
          for port in range(1, 1025):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            response = s.connect_ex((remoteServerIP, port))
            if response == 0:
                count=1    
                print ("Port " + str(port) + " open",end="")
                #makes educated guess on common protocols
                if port == 20 or port == 21:
                    print(" - FTP")
                elif port == 22:
                    print(" - SSH")
                elif port == 23:
                    print(" - Telnet")
                elif port == 25:
                    print(" - SMTP")
                elif port == 50 or port == 51:
                    print(" - IPSec")
                elif port == 53:
                    print(" - DNS")
                elif port == 67 or port == 68:
                    print(" - DHCP")
                elif port == 69:
                    print(" - TFTP")
                elif port == 80:
                    print(" - HTTP")
                elif port == 110:
                    print(" - POP3")
                elif port == 119:
                    print(" - NNTP")
                elif port == 123:
                    print(" - NTP")
                elif port in range(135,140):
                    print(" - NetBIOS")
                elif port == 143:
                    print(" - IMAP4")
                elif port == 161:
                    print(" - SNMP")
                elif port == 389:
                    print(" - LDAP")
                elif port == 443:
                    print(" - HTTPS")
                else:
                    print("")
          s.close()
          if(count==0):
             print("No open ports found")
        except KeyboardInterrupt:
          print ("You pressed CTRL+C")
          sys.exit()
        except socket.gaierror:
          print ("Hostname could not be resolved")
          sys.exit()
        except socket.error:
          print ("Couldn't connect to server")
          sys.exit()
          
        count=0
        print("Scan Complete")
        userinput=input("Would you like to scan again?: Y/N\n")
