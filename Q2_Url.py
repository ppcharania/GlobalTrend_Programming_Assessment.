import requests
from time import sleep

def download_content(urls):
    def fetch_url(url):
        attempts = 3
        for attempt in range(attempts):
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                return response.text
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err} - retrying {attempt+1}/{attempts}")
            except requests.exceptions.ConnectionError as conn_err:
                print(f"Connection error occurred: {conn_err} - retrying {attempt+1}/{attempts}")
            except requests.exceptions.Timeout as timeout_err:
                print(f"Timeout error occurred: {timeout_err} - retrying {attempt+1}/{attempts}")
            except requests.exceptions.RequestException as req_err:
                print(f"General error occurred: {req_err} - retrying {attempt+1}/{attempts}")
            sleep(1)  
        print(f"Failed to fetch {url} after {attempts} attempts")
        return None
    
    results = {}
    for url in urls:
        print(f"Fetching URL: {url}")
        content = fetch_url(url)
        results[url] = content
    
    return results

# Example usage:
urls = [
    "https://www.amazon.com",
    "https://www.google.com",
    "https://pc500.com"  
]

content_dict = download_content(urls)
for url, content in content_dict.items():
    if content:
        print(f"Content for {url} fetched successfully")
    else:
        print(f"Failed to fetch content for {url}")
