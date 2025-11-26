#!/usr/bin/python3
import random
import time
import requests

MAIN_URL = "http://127.0.0.1:8083"
URLS = ["/auth", "/pay", "/login", "/logout", "/refund", "/lk"]
METHODS = ["GET", "POST", "PUT", "DELETE"]

for i in range(1, 25):
    url = random.choice(URLS)
    method = random.choice(METHODS)
    full_url = f"{MAIN_URL}{url}"
    
    if method in ["GET", "DELETE"]:
        response = requests.request(method, full_url)
    else:
        data = {"sample_key": "sample_value", "iteration": i}
        response = requests.request(method, full_url, json=data)
    
    print(f"Request {method} on url {url}, response code {response.status_code}")
    time.sleep(2)
