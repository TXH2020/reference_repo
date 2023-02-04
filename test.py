import requests
r=requests.post('http://localhost:5000',{"hello":"three"})
print(r.text)

"""import subprocess
x=subprocess.Popen(['cmd'],text=True)
import json
import sys
import subprocess
command=json.loads(sys.argv[1]).get('Name')
call = subprocess.Popen(["bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, errors = call.communicate(input=command)
call.wait()
if(len(output)!=0):
	print(output)
if(len(errors)!=0):
	print(errors)"""
