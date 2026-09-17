import requests
import json
import os

url = "https://api.cloudability.com/v3/views/1892225"

payload = json.dumps({
  "title": "000 Test",
  "description": "",
  "filters": [
    {
      "field": "vendor_account_identifier",
      "comparator": "!=",
      "value": "f1b37eda-44be-419e-bb73-1d7c746af83a"
    },
    {
      "field": "vendor_account_identifier",
      "comparator": "!=",
      "value": "aa9e6f9d-d143-4c79-a7fa-4fb537cbbbc7"
    },
    {
      "field": "vendor",
      "comparator": "==",
      "value": "Azure"
    }
  ],
  "sharedOrgUnitIDs": [
    "36f05611-e458-4c45-92c6-6fe5ebef4a53"
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': f"{os.getenv("token")}"
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
