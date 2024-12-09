import requests

response = requests.get("http://localhost:8080/hello").json()

print(response)

#sucess