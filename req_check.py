import requests

print(requests.__version__)

resp = requests.get("http://google.com")
print(resp.text)
