#!/usr/bin/env python

import requests
import json

def is_json(response):
    try:
        json.loads(response)
    except ValueError as error:
        return False
    return True

def successful_response(status):
    if (status >= 300 or status < 200):
        return False
    else:
        return True

def post_hash(payload):
    url="http://127.0.0.1:8088/hash"
    headers = {'Content-Type': "application/json"}
    response = requests.request("POST", url, data=payload, headers=headers)
    return response, response.status_code

def get_hash_by_job(job_num):
    url="http://127.0.0.1:8088/hash/%d" %(job_num)
    response = requests.request("GET", url)
    return response, response.status_code

def get_hash_invalid():
    url="http://127.0.0.1:8088/hash"
    response = requests.request("GET", url)
    return response, response.status_code

def get_stats():
    url="http://127.0.0.1:8088/stats"
    response = requests.request("GET", url)
    return response, response.status_code

def get_stats_data_passed():
    url="http://127.0.0.1:8088/stats"
    data = {"password": "foo"}
    response = requests.get(url, data)
    return response, response.status_code

def post_stats():
    url="http://127.0.0.1:8088/stats"
    response = requests.request("POST", url)
    return response, response.status_code
