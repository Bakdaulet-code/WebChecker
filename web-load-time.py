import requests
import time

# The URL of the website to analyze
url = "https://www.example.com/"

# Send a GET request to the website and record the start time
start_time = time.time()
response = requests.get(url)

# Calculate the load time in seconds
load_time = time.time() - start_time

# Print the load time for demonstration purposes
print("Load time for", url, ":", load_time, "seconds")
