import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

# Loads the environment variables from the .env file
load_dotenv() 

# 1. Get the current date and time
now = datetime.now()

# 2. Format it into a safe string for file names (YYYY-MM-DD_HH-MM-SS)
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# 3. Create the filename
filename = f"view_backup_{timestamp}.json"

# 4. Create File Location
file_path = os.getenv("filepath") + filename

url = "https://api.cloudability.com/v3/views"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': f"{os.getenv("token")}"
}

response = requests.request("GET", url, headers=headers, data=payload)

# 2. Check that the request was successful
if response.status_code == 200:
    # 3. Convert the response into a Python dictionary/list
    data = response.json()

    # 4. Open a file in write mode ('w') and save the JSON data
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print(f"Successfully saved response to {filename}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

print(response.text)