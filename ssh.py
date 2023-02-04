import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.0.204", username='kali', password='kali')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('docker images')
print(ssh_stdout.read().decode())
print(ssh_stderr.read().decode())
ssh.close()
