import requests

print(requests.__version__)

resp = requests.get("https://raw.githubusercontent.com/Genna-C/CMPUT_404_lab1/main/req_check.py")
print(resp.text)
