from sys import stdout
import paramiko

hostname = '10.220.50.114'
username = 'root'
password = 'jlr173'

def send_sshcommand(cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(cmd)
    client.close()
    
def send_touch(x, y):
    send_sshcommand('otp/bin/touchinput -c tap -t 2 -p' + str(x) + ',' + str(y))