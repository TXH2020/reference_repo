import requests
r=requests.post('http://localhost:5000',{"hello":"three"})
print(r.text)