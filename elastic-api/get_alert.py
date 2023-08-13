import requests


api_key = "UWR6YjVJa0JVcmcyUXZuQms5eDM6SllpYTAxS2hRLTZtZllkNXdaNVhiQQ=="
url = "https://nosfera0x2.kb.us-central1.gcp.cloud.es.io:9243/api/detection_engine/rules?rule_id="
rule_id="1dee0500-4aeb-44ca-b24b-4a285d7b6ba1"
full_path = url+rule_id

headers = {
    'Content-Type': 'application/json;charset-UTF-8',
    'kbn-xsrf': 'true',
    'Authorization': 'ApiKey ' + api_key
}


elastic_data = requests.get(full_path, headers=headers).json()
print(elastic_data)