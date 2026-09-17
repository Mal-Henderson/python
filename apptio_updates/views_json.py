import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

# Loads the environment variables from the .env file
load_dotenv() 

# Location of view file downloaded from Apptio
viewfile = os.getenv("filepath")

# New filters as dictionary
new_filter1 = {
      "field": "vendor_account_identifier",
      "comparator": "!=",
      "value": "f1b37eda-44be-419e-bb73-1d7c746af83a",
    }
new_filter2 = {
      "field": "vendor_account_identifier",
      "comparator": "!=",
      "value": "aa9e6f9d-d143-4c79-a7fa-4fb537cbbbc7",
    }

# 1. Open and load the JSON file
with open(viewfile, "r") as file:
    data = json.load(file)

for _ , value in data.items():
    for view in value:
        id = view["id"]
        title = view["title"]
        description = view["description"]
        filters = view["filters"]
        filters.extend([new_filter1,new_filter2])
        sharedOrgUnitIDs = view["sharedOrgUnitIDs"]
        print(f"id: {id}")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Filters: {json.dumps(filters, indent=4)}")
        print(f"SharedOrgUnitIDs: {sharedOrgUnitIDs}")
        