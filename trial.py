
import requests
"""import time
def fp():
    with open('data.txt','r') as f:
        print(f.read())

for i in range(10):
    fp()
    with open('data.txt','a') as g:
        g.write('Hello'+str(i)+"\n")
    time.sleep(3)"""

parameters={'clear_authorized':'Yes'}
r=requests.post('http://localhost:5000/data',data=parameters)
print(r.text)