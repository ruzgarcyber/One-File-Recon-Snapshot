#One-File Recon Snapshot

import requests
import socket
import json

#Requests.
#HTTP request and status code.
url = "https://example.com"
response = requests.get(url)
status_code = response.status_code
for _ in range(10):
    try:
        r = requests.get(url)
        print(r.status_code)
        break
    except requests.exceptions.RequestException as e:
        print(e)
#Socket.
#IP çözümü.
ip_address = socket.gethostbyname("example.com")

#JSON.
#Sonuçları JSON olarak kaydetmek.
data = {"IP": ip_address, "Status Code": status_code}
with open("results.json", "w") as f:
    json.dump(data, f)
#IP List.
ip_list = ["1.1.1.1", "2.2.2.2", "3.3.3.3"]
#HTTP info.
def http_info(ip):
    url = f"http://{ip}"
    response = requests.get(url)
    return response.status_code
#HTTPS info.
def https_info(ip):
    url = f"https://{ip}"
    response = requests.get(url)
    return response.status_code

#Logging.
import logging
logging.basicConfig(filename="recon.log", level=logging.INFO)
logging.info("IP: %s, Status Code: %s", ip_address, status_code)
logging.error("Error: %s","None" )

#Argparse.
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", default="target.txt")
parser.add_argument("-o", "--output", default="results.txt")
args = parser.parse_args()

