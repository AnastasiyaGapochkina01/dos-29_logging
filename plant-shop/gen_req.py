#!/usr/bin/python3
import random
import time
import requests

MAIN_URL = "http://127.0.0.1"

PORTS = [8081, 8082]
URLS = ["/auth", "/pay", "/login", "/logout", "/refund", "/lk"]
METHODS = ["GET", "POST", "PUT", "DELETE"]

for i in range(1, 25):
    port = random.choice(PORTS)
    url = random.choice(URLS)
    method = random.choice(METHODS)
    
    full_url = f"{MAIN_URL}:{port}{url}"
    
    if method == "GET" or method == "DELETE":
        response = requests.request(method, full_url)
    else:
        data = {"sample_key": "sample_value", "iteration": i}
        response = requests.request(method, full_url, json=data)
    
    print(f"Request {method} on {port} url {url}, response code {response.status_code}")
    time.sleep(2)
