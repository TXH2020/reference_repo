import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.0.204", username='kali', password='kali')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('docker images')
print(ssh_stdout.read().decode())
print(ssh_stderr.read().decode())
ssh.close()

import requests
from flask import *
from flask_cors import CORS
import subprocess
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.0.204", username='kali', password='kali')
app=Flask(__name__)
CORS(app)
"""def get():
    #print(request.data)
    print(request.values.get('clear_authorized'))
    parameters={'clear_authorized':'Yes'}
    r=requests.post('http://localhost:8080/echo',data=parameters)
    print(r.text)
    return {"answer":"hello there"}"""
@app.route('/',methods=['POST'])
def get():
    print(request.data)
    x=json.loads(request.data.decode()).get("Name")
    if(x=="stop"):
        ssh.close()
        return {"Command_Output": "stopped"}
    _,command_output,_=ssh.exec_command(x)
    print(command_output)
    return {"Command_Output":command_output.read().decode()}

