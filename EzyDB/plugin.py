import requests
import json
from EzyDB.logmsg import Logger

log = Logger()
log.config(add_time=True, print_able=True)

def git_fetch(key, key2=None):
    # Step 1: Fetch the raw JSON file from GitHub
    url = "https://raw.githubusercontent.com/ezycode-org/EzyDB/refs/heads/main/plugins.json"
    response = requests.get(url)

    if response.status_code == 200:
        # Step 2: Parse the JSON content
        data = json.loads(response.text)

        # Step 3: Process the data
        if key2:
            value = data[key][key2]
        else:
            value = data[key]

        log.info(f"Plugin info has been fetched")

        return value
    
    else:
        log.error(f"Failed to fetch data from GitHub: {response.status_code}")
        return None

