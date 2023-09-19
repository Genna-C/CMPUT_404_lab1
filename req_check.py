import requests

print(requests.__version__)

resp = requests.get("https://github.com/Genna-C/CMPUT_404_lab1/blob/main/req_check.py")
print(resp.text)
