import os
import requests
import json

# Location of view file downloaded from Apptio
filepath = os.getenv("filepath")

# New filters as dictionary
new_filter = [{
      "field": "vendor_account_identifier",
      "comparator": "!=",
      "value": "f1b37eda-44be-419e-bb73-1d7c746af83a",
    },
{
      "field": "vendor_account_identifier",
      "comparator": "!=",
      "value": "aa9e6f9d-d143-4c79-a7fa-4fb537cbbbc7",
    }
]

# 1. Open and load the JSON file
with open(filepath, "r") as file:
    data = json.load(file)

# 2. Iterate over values in JSON file assigning variables for each iteration 
for _ , value in data.items():
    for field in value:
        id = field.get("id")
        title = field.get("title")
        description = field.get("description")
        ownerId = field.get("ownerId")
        sharedWithUsers = field.get("sharedWithUsers")
        derivedUserIds = field.get("derivedUserIds")
        derivedOrgUnitIDs = field.get("derivedOrgUnitIDs")
        sharedWithOrganization = field.get("sharedWithOrganization")            
        filters = field.get("filters")
        filters.extend(new_filter)
        sharedOrgUnitIDs = field.get("sharedOrgUnitIDs")
        ownerEmail = field.get("ownerEmail")
        
        # 3. Using View ID specify api endpoint for each view to be updated 
        url = f"https://api.cloudability.com/v3/views/{id}"

        # 4. Create full replace body for api call  
        payload = json.dumps({
        "title": title,
        "description": description,
        "ownerId": ownerId,
        "sharedWithUsers": sharedWithUsers,
        "derivedUserIds": derivedUserIds,
        "derivedOrgUnitIDs": derivedOrgUnitIDs,
        "sharedWithOrganization": sharedWithOrganization,
        "filters": filters,
        "sharedOrgUnitIDs": sharedOrgUnitIDs,
        "ownerEmail": ownerEmail})

        # 5. Specify headers for api call
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f"{os.getenv("token")}"
        }

        # 6. make View Update api call
        response = requests.request("PUT", url, headers=headers, data=payload)

        # 7. Print result of each iteration
        print(response.text)
