import requests
import json
<<<<<<< HEAD
from .logmsg import Logger
=======
from textPlay.logmsg import Logger
>>>>>>> ezydb/main

log = Logger()
log.config(add_time=True, print_able=True)

def git_fetch(*keys):
    """
    Fetches JSON data from the GitHub repository and retrieves the value for the specified keys.

    Args:
        *keys: A sequence of keys to navigate the nested JSON object.

    Returns:
        The value corresponding to the specified keys, or None if an error occurs.
    """
    # Step 1: Fetch the raw JSON file from GitHub
    url = "https://raw.githubusercontent.com/ezycode-org/EzyDB/refs/heads/main/plugins.json"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            # Step 2: Parse the JSON content
            data = json.loads(response.text)

            # Step 3: Navigate the nested JSON to get the value
            value = data
            for key in keys:
                value = value[key]  # Traverse each level with the given keys
            
            log.info("Plugin info has been fetched")
            return value

        except KeyError as e:
            log.error(f"Key error: {e}")
        except Exception as e:
            log.error(f"An error occurred while processing the JSON: {e}")

    else:
        log.error(f"Failed to fetch data from GitHub: {response.status_code}")
    
    return None
