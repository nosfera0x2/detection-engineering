import requests


api_key = "UWR6YjVJa0JVcmcyUXZuQms5eDM6SllpYTAxS2hRLTZtZllkNXdaNVhiQQ=="
url = "https://nosfera0x2.kb.us-central1.gcp.cloud.es.io:9243/api/detection_engine/rules"
headers = {
    'Content-Type': 'application/json;charset-UTF-8',
    'kbn-xsrf': 'true',
    'Authorization': 'ApiKey ' + api_key
}


elastic_data = requests.post(url, headers=headers,data=data).json()
print(elastic_data)