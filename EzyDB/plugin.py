import requests
import json
def git_fetch(key, key2=None):
    # Step 1: Fetch the raw JSON file from GitHub
    url = "https://raw.githubusercontent.com/ezycode-org/EzyDB/main/plugin.json"
    response = requests.get(url)

    if response.status_code == 200:
        # Step 2: Parse the JSON content
        data = json.loads(response.text)

        # Step 3: Process the data
        if key2:
            value = data[key][key2]
        else:
            value = data[key]

        return value
    
    else:
        print(f"Error fetching file: {response.status_code}")
        return None

