import socket
import subprocess
import sys
from datetime import datetime

## Clear the screen
subprocess.call('clear', shell=True)

## Enter Host to scan
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#This is just a nice touch that prints out information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

## Check what time the scan started
t1 = datetime.now()

## Using the range function to specify ports (here it will scans all ports between 1 and 1024)

## We also put in some error handling for catching errors

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            ## if a socket is listening it will print out the port number
            print("Port {}: \t Open".format(port))
            sock.close()

            ## Dont press any buttons or you will screw up the scanning, so i added a keyboard exception
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
    ## Here is my host execption, incase you typed it wrong. ( i guess mayeb i should have added this up top)
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()
    ## finally socket error incase python is having trouble scanning or resolving the port
except socket.error:
    print("Couldn't connect to server")
    sys.exit()

    ## Checking the time again
    t2 = datetime.now()

    ## Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    ## Printing the information to screen
    print('Scanning Completed in: ', total)
